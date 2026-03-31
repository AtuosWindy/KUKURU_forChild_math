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
        {"your_grade": 3, "nickname": "AAA", "score": 12000, "subject_name": "たしざん", "time": 5.15, "rate": 100},
        {"your_grade": 3, "nickname": "BBB", "score": 10000, "subject_name": "たしざん", "time": 5.15, "rate": 100},
        {"your_grade": 3, "nickname": "CCC", "score": 8000, "subject_name": "たしざん", "time": 5.15, "rate": 100},
    ]

    return templates.TemplateResponse(
        request,
        name="ranking.html",
        context={
            "request": request,
            "ranking": rankings
        }
    )