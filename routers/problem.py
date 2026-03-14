from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from engine.generator import generate_problem

router = APIRouter()

templates = Jinja2Templates(directory="templates")


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

    index = request.session.get("index", 0)
    problems = request.session.get("problems", [])
    difficulty = request.session.get("difficulty", 1)

    problem = problems[index]

    if index >= len(problems):
        return {"status": "finished"}

    problem = problems[index]

    request.session["index"] = index + 1

    return {
        "problem": problem,
        "difficulty": difficulty,
    }


@router.get("/result")
def result(request: Request, time: float, rate: float):
    return templates.TemplateResponse(
        "result.html",
        {"request": request, "time": time, "rate": rate}
    )