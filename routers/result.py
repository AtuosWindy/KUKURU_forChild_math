from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from engine.generator import generate_problem

router = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get("/result", response_class=HTMLResponse)
def result(request: Request):
    return templates.TemplateResponse()