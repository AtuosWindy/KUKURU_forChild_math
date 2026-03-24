from fastapi import APIRouter, FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/result", response_class=HTMLResponse)
def result(request: Request):
    request.session["initialized"] = False
    return templates.TemplateResponse(
        request,
        name = "result.html",
        context = {
            "request": request,
            "time": request.session.get("time", 0),
            "rate": request.session.get("rate", 0),
            "score": request.session.get("score", 0),
        }
    )