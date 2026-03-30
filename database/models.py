from sqlalchemy import Column, Integer, Float, String
from .db import Base


class Ranking(Base):
    __tablename__ = "rankings"

    id = Column(Integer, primary_key=True, index=True)

    nickname = Column(String, nullable=False)
    your_grade = Column(Integer, nullable=True)

    subject_name = Column(String)
    difficulty = Column(Integer)
    problem_count = Column(Integer)

    rate = Column(Float)
    time = Column(Float)
    score = Column(Float)