from fastapi import APIRouter

router = APIRouter()

@router.get("/ranking")
def get_ranking():
    return {"message": "ranking"}