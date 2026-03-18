from re import S
from tokenize import Double
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from engine.generator import generate_problem

router = APIRouter()

templates = Jinja2Templates(directory="templates")


class AnswerRequest(BaseModel):
    answer: str


@router.get("/problem", response_class=HTMLResponse)
def problem_page(request: Request):

    return templates.TemplateResponse(
        "problem.html",
        {
            "request": request,
            "count": request.session["count"]
        }
    )


@router.get("/api/problem")
def get_problem(request: Request):

    difficulty = request.session.get("difficulty", 1)

    problem_count = request.session.get("problem_count", 0)
    wrong_problem_count = request.session.get("wrong_problem_count", 0)

    problems = request.session.get("problems", [])
    wrong_problems = request.session.get("wrong_problems", [])
    index = request.session.get("index", 0)

    correct = request.session.get("correct", 0)

    miss_flag = request.session.get("miss_flag", False)
    retry_flag = request.session.get("retry_flag", False)

    # retryの場合は間違えた問題を解きなおすため、出題数を切り替える
    p_num = problem_count if not retry_flag else wrong_problem_count

    if index >= p_num:    # 全問解き終わった場合の処理
        #
        # 疑似コード↓
        if retry_flag:  # すでに解きなおししてる場合
            i = 0
        #   /result へ行く処理を追加する
        else:  # まだ解きなおししてない場合は、全問解き終わったけど、間違えた問題があるかもしれないので、その場合は解きなおすか問う。タイムはとめる。
            start_time = request.session["start_time"]
            stop_time = start_time  # タイムをとめる
            time = stop_time - start_time
            request.session["stop_time"] = stop_time    #機能的に意味はそこまでないが、コードの構造上あったほうが分かりやすく、さらに将来的に不正操作があった場合のデバッグ材料になるため記録する。
            rate = int(correct / problem_count * 100)
            grade = request.session["grade"]
            subject = request.session["subject"]
            # problem_count は冒頭でセッションから取得しているからOK！
            score = calculate_score(grade, subject, difficulty, problem_count, rate, time) # スコアの計算式は要検討。とりあえず、正答率と時間をもとに、スコアを計算する感じでいいと思う。良い値ほど高くする。ランキングの順位は最終的にコレ１つで決める。超重要。
            request.session["time"] = time
            request.session["rate"] = rate
            request.session["score"] = score
            if miss_flag:  # 間違えた問題がある場合
                #ユーザに「問題を解きなおすかどうか尋ねる」
                #if 「問題を解きなおすかどうか尋ねた結果、ユーザが「解きなおす」と答えた場合」:
                    retry_flag = True
                    index = 0   # 間違えた問題を解きなおす場合に備え、indexをリセット
                    request.session["retry_flag"] = retry_flag
                    request.session["index"] = index
                    request.session["wrong_problem_count"] = len(wrong_problems)
                    #↓if分岐を抜けた p_list にて、間違えた問題をリスト0番目から再度解き始める処理が開始
            else:  # 間違えた問題がない場合は、解きなおす必要ないので、そのまま/resultへ行く
                i = 0
                #/result へ行く処理を追加する

        
        return {"status": "finished"}

    # retryの場合は間違えた問題を解きなおすため、問題リストを切り替える
    p_list = problems if not retry_flag else wrong_problems

    problem = p_list[index]

    return {
        "problem": problem,
    }

def calculate_score(grade: int, subject: int, difficulty: int, problem_count: int, rate: int, time):

    # 計算基準
    # ① 計算ステップ数
    # 足し算 → 1〜2手
    # 筆算 → 3〜6手
    # 分数 → 4〜8手
    # 
    # ② 認知負荷（考える量）
    # 九九 → 低い（暗記）
    # 分数 → 高い（通分など）
    # 文字式 → 中（概念理解）
    # 
    # ③ 入力コスト
    # 選択式 → 速い
    # 入力式 → 遅い
    BASE_TIME_MAP = {
        # --- grade1 ---
        1001: 2.5,  # たしざん
        1002: 2.5,  # ひきざん
        1003: 3.5,  # 繰り上がり
        1004: 3.5,  # 繰り下がり

        # --- grade2 ---
        2001: 4.0,  # 2桁たし算
        2002: 4.0,  # 2桁ひき算
        2003: 6.0,  # 筆算
        2004: 2.5,  # 九九（暗記）

        # --- grade3 ---
        3001: 5.0,  # 3桁
        3002: 5.5,  # かけ算
        3003: 5.5,  # わり算
        3004: 6.5,  # あまりあり

        # --- grade4 ---
        4001: 6.5,  # 2桁×2桁
        4002: 6.0,  # わり算
        4003: 8.0,  # わり算筆算（重い）
        4004: 6.0,  # 小数

        # --- grade5 ---
        5001: 7.0,  # 小数×小数
        5002: 7.5,  # 小数÷小数
        5003: 8.5,  # 分数＋
        5004: 8.5,  # 分数−

        # --- grade6 ---
        6001: 9.0,  # 分数×
        6002: 9.5,  # 分数÷
        6003: 5.0,  # 文字式（計算軽い）
        6004: 10.0, # 総合（MAX）
    }

    # 難易度係数、算出方法
    # ① 計算量（0〜1.0）
    # 桁数・手数
    # 
    # ② 概念難易度（0〜0.8）
    # 分数・文字式など
    # 
    # ③ ミス誘発（0〜0.6）
    # 繰り上がり・あまりなど
    DIFFICULTY_MAP = {
        # --- grade1 ---
        1001: 1.0,  # たしざん（最小）
        1002: 1.0,  # ひきざん

        1003: 1.2,  # calc0.2 + trap0.0（繰り上がり）
        1004: 1.3,  # calc0.2 + trap0.1（繰り下がりの方がミスりやすい）

        # --- grade2 ---
        2001: 1.3,  # calc0.3
        2002: 1.3,

        2003: 1.5,  # calc0.4 + trap0.1（筆算ズレ）
        2004: 1.1,  # concept0.1（暗記）

        # --- grade3 ---
        3001: 1.5,  # calc0.5
        3002: 1.6,  # calc0.5 + concept0.1
        3003: 1.6,  # calc0.5 + concept0.1

        3004: 1.8,  # calc0.5 + concept0.1 + trap0.2（あまり）

        # --- grade4 ---
        4001: 1.8,  # calc0.7 + concept0.1
        4002: 1.7,  # calc0.6 + concept0.1

        4003: 2.0,  # calc0.7 + trap0.3（筆算地獄）
        4004: 1.7,  # calc0.5 + concept0.2（小数）

        # --- grade5 ---
        5001: 1.9,  # calc0.6 + concept0.3
        5002: 2.0,  # calc0.6 + concept0.3 + trap0.1

        5003: 2.1,  # calc0.5 + concept0.5 + trap0.1（通分）
        5004: 2.2,  # calc0.5 + concept0.5 + trap0.2（借り）

        # --- grade6 ---
        6001: 2.3,  # calc0.6 + concept0.5 + trap0.2
        6002: 2.4,  # calc0.6 + concept0.5 + trap0.3（逆数ミス）

        6003: 1.8,  # calc0.2 + concept0.6（理解ゲー）
        6004: 2.8,  # 全部盛り
    }
    import math

    # 難易度係数
    submit_type = {
        1: 1.0,   # かんたん（選択）
        2: 1.2,   # ふつう
        3: 1.35,  # むずかしい
    }[difficulty]
    d_num = DIFFICULTY_MAP[grade * 1000 + subject] * submit_type

    # ベース時間
    base_time = BASE_TIME_MAP[grade * 1000 + subject] * problem_count

    # スピード
    time_correction = max(time, 1.0)
    speed = max(0.3, math.log(1 + base_time / time_correction))

    # 正答率補正(子供の心が折れないため)
    r_correction = max(rate, 0.3) / 100

    # スコア
    score = (
        d_num
        * (r_correction ** 3)
        * speed
        * math.sqrt(problem_count)
    )

    #算出方法はゲーム業界とかが採用してるようなガチなやつを取り入れようかと検討中。
    return int(score * 1000)  # スコアは整数で、かつ良い値ほど大きくなるように調整


@router.post("/api/answer")
def answer(request: Request, body: AnswerRequest):
    user_answer = body.answer

    index = request.session["index"]
    problems = request.session["problems"]
    wrong_problems = request.session["wrong_problems"]
    retry_flag = request.session["retry_flag"]

    p_list = problems if not retry_flag else wrong_problems
    correct_answer = p_list[index]["answer"]

    miss_flag = request.session["miss_flag"]
    retry_flag = request.session["retry_flag"]

    is_correct = user_answer == correct_answer
    if not is_correct:
        if not retry_flag:  # 解きなおしは１回のみ！！
            request.session["wrong_problems"].append(p_list[index])
        if not miss_flag:   # 問題間違えた ＆ まだ miss_flag が立ってない場合、 miss_flag を立てる
            miss_flag = True
            request.session["miss_flag"] = miss_flag
    else:
        request.session["correct"] += 1

    request.session["index"] += 1

    # ここで/api/problem呼ぶ！

    return {"is_correct": is_correct}


@router.get("/result")
def result(request: Request, time: float, rate: float):
    return templates.TemplateResponse(
        "result.html",
        {"request": request, "time": time, "rate": rate}
    )