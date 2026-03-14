import random
from .basic_routine import value_each_difficulty


#difficulty - 1(かんたん)~3(むずかしい)

#1年生, 1桁の足し算(繰り上がりなし→答えが1桁)
def subject_1001(difficulty: int):
    #難易度調整
    value = value_each_difficulty(difficulty, 1, 1, 1)
    if value == -1:
        return -1, "error", -1, -1, -1

    #2値を決める
    a = random.randint(value,8)
    b = random.randint(value,9-a)

    return {
        "a": a,
        "op": "+",
        "b": b,
        "answer": a + b,
        "answer_type": "int",
        "q_type": "normal",
    }


#1年生, 1桁の引き算
def subject_1002(difficulty: int):
    #難易度調整
    value = value_each_difficulty(difficulty, 1, 1, 1)
    if value == -1:
        return -1, "error", -1, -1, -1

    #2値を決める
    a = random.randint(value,9)
    b = random.randint(value,a)

    return {
        "a": a,
        "op": "-",
        "b": b,
        "answer": a - b,
        "answer_type": "int",
        "q_type": "normal",
    }


#1年生, 繰り上がりのある足し算
def subject_1003(difficulty: int):
    #難易度調整
    value = value_each_difficulty(difficulty, 1, 1, 1)
    if value == -1:
        return -1, "error", -1, -1, -1

    #2値を決める
    a = random.randint(value,9)
    b = random.randint(10-a,9)

    return {
        "a": a,
        "op": "+",
        "b": b,
        "answer": a + b,
        "answer_type": "int",
        "q_type": "normal",
    }


#1年生, 繰り下がりのある引き算
def subject_1004(difficulty: int):
    #難易度調整
    value = value_each_difficulty(difficulty, 1, 1, 1)
    if value == -1:
        return -1, "error", -1, -1, -1

    #2値を決める
    b = random.randint(1,9)
    a = random.randint(10,9+b)

    return {
        "a": a,
        "op": "-",
        "b": b,
        "answer": a - b,
        "answer_type": "int",
        "q_type": "normal",
    }