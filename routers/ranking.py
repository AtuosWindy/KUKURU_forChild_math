from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database.db import get_db
from database import crud

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/ranking", response_class=HTMLResponse)
def get_ranking(request: Request, db: Session = Depends(get_db)):

    # 仮データ（あとでDBに置き換える）
    rankings = crud.get_rankings_all(db)

    ranking = [
        {"nickname": "AAA", "score": 12000},
        {"nickname": "BBB", "score": 10000},
        {"nickname": "CCC", "score": 8000},
    ]

    return templates.TemplateResponse(
        "ranking.html",
        {
            "request": request,
            "ranking": ranking
        }
    )