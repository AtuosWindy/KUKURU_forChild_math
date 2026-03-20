import random
from engine.subjects.subject_map import SUBJECT_MAP
from engine.choices import integer
from engine.choices import decimal
from engine.choices import remain
from engine.choices import fraction


def generate_problem(grade: int, subject: int, difficulty: int):
    print("DEBUG:", grade, subject, difficulty)

    data = SUBJECT_MAP[grade * 1000 + subject]

    func = data["func"]
    problem = func(difficulty)

    count = data["count"][difficulty - 1]

    a = problem["a"]
    op = problem["op"]
    b = problem["b"]
    answer = problem["answer"]
    answer_type = problem["answer_type"]
    q_type = problem["q_type"]

    print("answer_type =", answer_type)

    if q_type == "normal":
        question = f"{a} {op} {b} = ?"
    elif q_type == "left_op":
        question = f"? {op} {a} = {b}"
    elif q_type == "right_op":
        question = f"{a} {op} ? = {b}"

    if answer_type == "int":
        choices = integer.generate(answer)

    elif answer_type == "dec":
        choices = decimal.generate(answer)

    elif answer_type == "rem":
        choices = remain.generate(answer)

        q = answer["q"]
        r = answer["r"]

        if r == 0:
            answer = f"{q}"
        else:
            answer = f"{q}あまり{r}"

    elif answer_type == "fra":

        choices = fraction.generate(answer)

        answer = str(answer)
        choices = [str(c) for c in choices]

    else:
        raise ValueError(f"Unknown answer_type: {answer_type}")

    random.shuffle(choices)

    print("⇒  ", question, ", ", answer)

    return {
        "question": question,
        "choices": choices,
        "answer": str(answer),
        "answer_type": answer_type,
        "difficulty": difficulty
    }