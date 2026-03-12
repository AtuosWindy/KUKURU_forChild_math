from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from engine.generator import generate_problem

router = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get("/home", response_class=HTMLResponse)
def home(
    request: Request,
    grade: int | None = None,
    subject: int | None = None
):

    return templates.TemplateResponse(
        "home.html",
        {
            "request": request,
            "grade": grade,
            "subject": subject
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

    for _ in range(10):
        problems.append(
            generate_problem(grade, subject, difficulty)
        )

    request.session["grade"] = grade
    request.session["subject"] = subject
    request.session["difficulty"] = difficulty

    request.session["index"] = 0
    request.session["problems"] = problems

    return RedirectResponse("/problem", status_code=303)
