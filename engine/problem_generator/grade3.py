import random
from .basic_routine import value_each_difficulty


#difficulty - 1(かんたん)~3(むずかしい)

#3桁の足し算
def add_3digits(difficulty: int):
    #難易度調整
    value = value_each_difficulty(difficulty, 300, 450, 999)
    if value == -1:
        return -1, "error", -1, -1, -1

    #2値を決める
    a = random.randint(100,value)
    b = random.randint(100,value)

    return {
        "a": a,
        "op": "+",
        "b": b,
        "answer": a + b,
        "answer_type": "int",
        "q_type": "normal",
    }


#3桁の引き算
def sub_3digits(difficulty: int):
    #難易度調整
    value = value_each_difficulty(difficulty, 300, 450, 999)
    if value == -1:
        return -1, "error", -1, -1, -1

    #2値を決める
    a = random.randint(100,value)
    b = random.randint(100,a)

    return {
        "a": a,
        "op": "-",
        "b": b,
        "answer": a - b,
        "answer_type": "int",
        "q_type": "normal",
    }


#3年生, 3桁の足し算・引き算
def subject_3001(difficulty: int):
    op = random.choice(["+", "-"])

    #難易度調整は、if分岐の中で呼び出される関数内で行われる。
    if op == "+":
        return add_3digits(difficulty)
    else:
        return sub_3digits(difficulty)


#3年生, かけ算（2桁 × 1桁）
def subject_3002(difficulty: int):
    #難易度調整
    value   = value_each_difficulty(difficulty, 19, 35, 99)
    value2 = value_each_difficulty(difficulty, 1, 1, 4)
    if value == -1 or value2 == -1:
        return -1, "error", -1, -1, -1

    #2値を決める
    a = random.randint(10,value)
    b = random.randint(value2,9)

    return {
        "a": a,
        "op": "×",
        "b": b,
        "answer": a * b,
        "answer_type": "int",
        "q_type": "normal",
    }


#3年生, わり算（1桁）
def subject_3003(difficulty: int):
    #難易度調整
    value   = value_each_difficulty(difficulty, 19, 45, 81)
    value2 = value_each_difficulty(difficulty, 2, 5, 9)
    if value == -1 or value2 == -1:
        return -1, "error", -1, -1, -1

    #2値を決める
    b = random.randint(1,value2)
    a = random.randint(b,b*9)

    return {
        "a": a,
        "op": "÷",
        "b": b,
        "answer": a // b,
        "answer_type": "int",
        "q_type": "normal",
    }


#3年生, あまりのあるわり算
def subject_3004(difficulty: int):
    #難易度調整
    value   = value_each_difficulty(difficulty, 19, 49, 89)
    value2 = value_each_difficulty(difficulty, 3, 6, 9)
    if value == -1 or value2 == -1:
        return -1, "error", -1, -1, -1

    #2値を決める
    b = random.randint(2,value2)
    r = random.randint(1,b-1)
    q = random.randint(1,9)
    a = q * b + r

    #答えを算出する
    answer = {
        "q": q,
        "r": r,
        "b": b,
    }

    return {
        "a": a,
        "op": "÷",
        "b": b,
        "answer": answer,
        "answer_type": "rem",
        "q_type": "normal",
    }