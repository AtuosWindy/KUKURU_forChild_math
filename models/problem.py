class Problem(BaseModel):
    question: str
    choices: list[str]
    answer: str