import random
from .basic_routine import value_each_difficulty


#difficulty - 1(かんたん)~3(むずかしい)

#少数の足し算
def add_floats(difficulty: int):
    #難易度調整
    value   = value_each_difficulty(difficulty, 10.0, 10.0, 15.0)
    value2 = value_each_difficulty(difficulty, 0.0, 4.0, 6.0)
    if value == -1 or value2 == -1:
        return -1, "error", -1, -1, -1

    #2値を決める
    a = round(random.uniform(value2, value), 1)
    b = round(random.uniform(value2, value), 1)

    return {
        "a": a,
        "op": "+",
        "b": b,
        "answer": round(a + b, 1),
        "answer_type": "dec",
        "q_type": "normal",
    }


#少数の引き算
def sub_floats(difficulty: int):
    #難易度調整
    value   = value_each_difficulty(difficulty, 10.0, 10.0, 15.0)
    value2 = value_each_difficulty(difficulty, 0.0, 4.0, 6.0)
    if value == -1 or value2 == -1:
        return -1, "error", -1, -1, -1

    #2値を決める
    a = round(random.uniform(value2, value), 1)
    b = round(random.uniform(value2, a), 1)

    return {
        "a": a,
        "op": "-",
        "b": b,
        "answer": round(a - b, 1),
        "answer_type": "dec",
        "q_type": "normal",
    }


#4年生, かけ算（2桁 × 2桁）
def subject_4001(difficulty: int):
    #難易度調整
    value   = value_each_difficulty(difficulty, 19, 35, 99)
    if value == -1:
        return -1, "error", -1, -1, -1

    #2値を決める
    a = random.randint(10,value)
    b = random.randint(10,value)

    return {
        "a": a,
        "op": "×",
        "b": b,
        "answer": a * b,
        "answer_type": "int",
        "q_type": "normal",
    }


#4年生, わり算（2桁 ÷ 1桁）
def subject_4002(difficulty: int):
    #難易度調整
    value   = value_each_difficulty(difficulty, 19, 35, 99)
    value2 = value_each_difficulty(difficulty, 1, 1, 4)
    if value == -1 or value2 == -1:
        return -1, "error", -1, -1, -1

    #2値を決める
    b = random.randint(value2,9)
    count100 = 1
    count10 = 1
    count10_flag = 0
    a = b
    while a < 100:
        if count100 > 1:
            count100 += 1
            a = b
        a *= count100
        if a > 10 and count10_flag == 0:
            count10 = count100
            count10_flag = 1

    count100 -= -1
    mul = random.randint(count10,count100)
    a = b*mul

    return {
        "a": a,
        "op": "÷",
        "b": b,
        "answer": a // b,
        "answer_type": "int",
        "q_type": "normal",
    }


#4年生, わり算（筆算）
def subject_4003(difficulty: int):
    #難易度調整
    value   = value_each_difficulty(difficulty, 99, 450, 999)
    value2 = value_each_difficulty(difficulty, 1, 1, 1)
    value3 = value_each_difficulty(difficulty, 45, 450, 999)
    if value == -1 or value2 == -1 or value3 == -1:
        return -1, "error", -1, -1, -1

    #2値を決める
    b = random.randint(value2,value3)
    a = random.randint(b, value)
    answer = {
        "q": a // b,
        "r": a % b,
    }

    return {
        "a": a,
        "op": "÷",
        "b": b,
        "answer": a // b,
        "answer_type": "rem",
        "q_type": "normal",
    }


#4年生, 小数の足し算・引き算
def subject_4004(difficulty: int):
    op = random.choice(["+", "-"])

    #難易度調整は、if分岐の中で呼び出される関数内で行われる。
    if op == "+":
        return add_floats(difficulty)
    else:
        return sub_floats(difficulty)