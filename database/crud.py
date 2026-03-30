from sqlalchemy import exc
from sqlalchemy.orm import Session
from .models import Ranking


def create_ranking(db: Session, data: dict):
    try:
        ranking = Ranking(**data)
        db.add(ranking)
        # db.flush()
        db.commit()
        db.refresh(ranking)
    except Exception as e:
        db.rollback()
        print("DBエラー", e)

    db.close()

    return ranking


def get_rankings_all(db: Session, limit: int = 100):
    return db.query(Ranking).order_by(Ranking.score.desc()).limit(limit).all()


def get_rankings_by_grade(db: Session, grade: int):
    return (
        db.query(Ranking)
        .filter(Ranking.your_grade == grade)
        .order_by(Ranking.score.desc())
        .all()
    )