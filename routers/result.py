from fastapi import APIRouter, FastAPI, Request, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import exc
from sqlalchemy.orm import Session
from database.db import get_db
from database import crud

import time

router = APIRouter()

templates = Jinja2Templates(directory="templates")



@router.get("/result", response_class=HTMLResponse)
def result(request: Request):
    # result の URL 直打ち対策
    if request.session.get("score") == -1:
        return RedirectResponse("/home")

    print(request.session.get("nickname", ""))
    return templates.TemplateResponse(
        request,
        name = "result.html",
        context = {
            "request": request,
            "nickname": request.session.get("nickname", ""),
            "subject_name": request.session.get("subject_name", ""),
            "time": request.session.get("time", 0),
            "rate": request.session.get("rate", 0),
            "score": request.session.get("score", 0),
        }
    )


@router.post("/api/register")
async def save_result(request: Request, db: Session = Depends(get_db)):
    try:
        body = await request.json()
        nickname = body.get("nickname")

        if nickname and nickname != request.session.get("nickname"):
            request.session["nickname"] = nickname

        data = {
            "nickname": request.session.get("nickname"),
            "your_grade": request.session.get("your_grade"),

            "subject_name": request.session.get("subject_name"),
            "difficulty": request.session.get("difficulty"),
            "problem_count": request.session.get("problem_count"),

            "rate": request.session.get("rate"),
            "time": request.session.get("time"),
            "score": request.session.get("score"),
        }

        crud.create_ranking(db, data)

        # request.session["score"] = -1

        if request.session.get("already_registered"):
            return {"status": "ok"}

        request.session["already_registered"] = True

        return {"status": "ok"}
    except Exception as e:
        print("DBエラー", e)
        time.sleep(0.2)
        return {"status": "retry"}