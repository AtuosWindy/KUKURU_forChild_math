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
        #   stop_time = ...  # タイムをとめる
        #   time = stop_time - start_time
        #   request.session["stop_time"] = stop_time    #機能的に意味はそこまでないが、コードの構造上あったほうが分かりやすく、さらに将来的に不正操作があった場合のデバッグ材料になるため記録する。
        #   request.session["time"] = time
            rate = correct / problem_count * 100
            grade = request.session["grade"]
            subject = request.session["subject"]
            # problem_count は冒頭でセッションから取得しているからOK！
        #   score = calculate_score(grade, subject, problem_count, rate, time) # スコアの計算式は要検討。とりあえず、正答率と時間をもとに、スコアを計算する感じでいいと思う。良い値ほど高くする。ランキングの順位は最終的にコレ１つで決める。超重要。
        #   request.session["time"] = time
            request.session["rate"] = rate
        #   request.session["score"] = score
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

def calculate_score(grade: int, subject: int, problem_count: int, rate, time):
    score  = 0
    #算出方法はゲーム業界とかが採用してるようなガチなやつを取り入れようかと検討中。
    return score

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