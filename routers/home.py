from fastapi import APIRouter, FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from pydantic import BaseModel

from engine.generator import SUBJECT_MAP, generate_problem
from engine.subjects import grade1

import time

router = APIRouter()

templates = Jinja2Templates(directory="templates")


class StartRequest(BaseModel):
    grade: int
    subject: int
    difficulty: int


@router.get("/home", response_class=HTMLResponse)
def home(
    request: Request,
    grade: int | None = None,
    subject: int | None = None
):

    subject_names = {}

    # セッションの初期化
    if "initialized" not in request.session:
        request.session["grade"] = 1
        request.session["subject_number"] = 1
        request.session["difficulty"] = 1

        request.session["subject_name"] = ""
        request.session["problem_count"] = 0
        request.session["wrong_problem_count"] = 0

        request.session["problems"] = []  # 正解込み
        request.session["wrong_problems"] = []  # 間違えのみ
        request.session["index"] = 0
        request.session["correct"] = 0
        request.session["miss_flag"] = False
        request.session["retry_flag"] = False

        request.session["rate"] = 0.0
        request.session["start_time"] = 0
        request.session["end_time"] = 0
        request.session["time"] = 0
        request.session["score"] = 0
        request.session["rank"] = 0

        request.session["initialized"] = True


    if grade:
        subject_names = {
            k: v["name"]
            for k, v in SUBJECT_MAP.items()
            if k // 1000 == grade
        }

    return templates.TemplateResponse(
        request,
        name = "home.html",
        context = {
            "request": request,
            "subject_map": SUBJECT_MAP,
        }
    )


@router.post("/api/start")
def start(
    request: Request,
    data: StartRequest
):
    grade = data.grade
    subject = data.subject
    difficulty = data.difficulty

    # 問題生成
    problems = []

    data_map = SUBJECT_MAP[grade * 1000 + subject]
    count = data_map["count"][difficulty - 1]

    for _ in range(count):
        problems.append(
            generate_problem(grade, subject, difficulty)
        )

    #セッションに保存
    request.session["grade"] = grade
    request.session["subject_number"] = subject
    request.session["difficulty"] = difficulty

    request.session["subject_name"] = data_map["name"]
    request.session["problem_count"] = int(count)
    print("home.pyの/api/startにて, ", count, " がproblem_countに保存されました。")
    request.session["wrong_problem_count"] = 0

    request.session["problems"] = problems  # 正解込み
    request.session["wrong_problems"] = []  # 間違えのみ
    request.session["index"] = 0
    request.session["correct"] = 0
    request.session["miss_flag"] = False
    request.session["retry_flag"] = False

    request.session["rate"] = 0.0
    request.session["start_time"] = time.time()
    request.session["end_time"] = 0
    request.session["time"] = 0
    request.session["score"] = 0
    request.session["rank"] = 0

    # request.session["your_grade"] = 0
    request.session["nickname"] = ""

