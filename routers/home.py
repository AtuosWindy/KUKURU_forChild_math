from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from engine.generator import SUBJECT_MAP, generate_problem

router = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get("/home", response_class=HTMLResponse)
def home(
    request: Request,
    grade: int | None = None,
    subject: int | None = None
):

    subject_names = None

    if grade:
        subject_names = {
            k: v["name"]
            for k, v in SUBJECT_MAP.items()
            if k // 1000 == grade
        }

    return templates.TemplateResponse(
        "home.html",
        {
            "request": request,
            "grade": grade,
            "subject": subject,
            "subject_names": subject_names
        }
    )

@router.get("/start")
def start(
    request: Request,
    grade: int,
    subject: int,
    difficulty: int
):

    problems = []

    data = SUBJECT_MAP[grade * 1000 + subject]
    count = data["count"][difficulty - 1]

    for _ in range(count):
        problems.append(
            generate_problem(grade, subject, difficulty)
        )

    request.session["grade"] = grade
    request.session["subject"] = subject
    request.session["difficulty"] = difficulty
    request.session["count"] = count

    request.session["index"] = 0
    request.session["problems"] = problems

    return RedirectResponse("/problem", status_code=303)
