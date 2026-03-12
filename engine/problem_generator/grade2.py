import random
from .basic_routine import value_each_difficulty


#difficulty - 1(かんたん)~3(むずかしい)

#2年生, 2桁の足し算
def subject_2001(difficulty: int):
    #難易度調整
    value = value_each_difficulty(difficulty, 19, 35, 99)
    if value == -1:
        return -1, "error", -1, -1, -1

    #2値を決める
    a = random.randint(10,value)
    b = random.randint(10,value)

    return {
        "a": a,
        "op": "+",
        "b": b,
        "answer": a + b,
        "answer_type": "int",
        "q_type": "normal",
    }


#2年生, 2桁の引き算
def subject_2002(difficulty: int):
    #難易度調整
    value = value_each_difficulty(difficulty, 19, 35, 99)
    if value == -1:
        return -1, "error", -1, -1, -1

    #2値を決める
    a = random.randint(10,value)
    b = random.randint(10,a)

    return {
        "a": a,
        "op": "-",
        "b": b,
        "answer": a - b,
        "answer_type": "int",
        "q_type": "normal",
    }


#2年生, 筆算(mix)
def subject_2003(difficulty: int):
    op = random.choice(["+", "-"])

    #難易度調整は、if分岐の中で呼び出される関数内で行われる。
    if op == "+":
        return subject_2001(difficulty)
    else:
        return subject_2002(difficulty)


#2年生, 九九
def subject_2004(difficulty: int):
    #難易度調整
    value = value_each_difficulty(difficulty, 2, 5, 9)
    if value == -1:
        return -1, "error", -1, -1, -1

    #2値を決める
    a = random.randint(1,value)
    b = random.randint(1,9)

    return {
        "a": a,
        "op": "×",
        "b": b,
        "answer": a * b,
        "answer_type": "int",
        "q_type": "normal",
    }