import random
import math
from fractions import Fraction
from .basic_routine import value_each_difficulty


#difficulty - 1(かんたん)~3(むずかしい)

#5年生, 小数 × 小数
def subject_5001(difficulty: int):
    #難易度調整
    value   = value_each_difficulty(difficulty, 9.9, 9.9, 9.9)	#問題数で難易度調整とする
    value2 = value_each_difficulty(difficulty, 0.1, 0.1, 0.1)
    if value == -1 or value2 == -1:
        return -1, "error", -1, -1, -1

    #2値を決める
    a = round(random.uniform(value2, value), 1)
    b = round(random.uniform(value2, value), 1)

    #答えの小数点以下桁数を整える
    answer = int(round(a*b, 2) * 100)
    digit = 0	#answerの小数点以下桁数
    if answer % 100 == 0:
        digit = 0
        answer = int(answer)
    else:
        if answer % 10 == 0:
            digit = 1
        else:
            digit = 2

        answer = round(answer/100, digit)


    return {
        "a": a,
        "op": "×",
        "b": b,
        "answer": answer,
        "answer_type": "dec",
        "q_type": "normal",
    }


#5年生, 小数 ÷ 小数
def subject_5002(difficulty: int):
    #難易度調整
    value   = value_each_difficulty(difficulty, 99.9, 99.9, 99.9)	#問題数で難易度調整とする
    value2 = value_each_difficulty(difficulty, 0.1, 0.1, 0.1)
    value3 = value_each_difficulty(difficulty, 9.9, 9.9, 9.9)
    if value == -1 or value2 == -1 or value3 == -1:
        return -1, "error", -1, -1, -1

    #2値を決めながら、答えの小数点以下桁数を整える
    b = round(random.uniform(value2, value3), 1)

    answer_limit = value/b
    digits_a = 3		#bが小数点以下1桁固定・基本はanswerが2桁⇒基本はaは小数点以下３桁
    answer = round(random.uniform(1, answer_limit), 2)	#基本は答えが小数点以下2桁になる予定
    if round(answer,1) == answer:		#偶然小数点以下1桁になった場合、1桁に整える
        digits_a = 2					#answerが小数点以下1桁になった時だけaは小数点以下２桁になる
        answer = round(answer, 1)

    a = round(b * answer, digits_a)

    return {
        "a": a,
        "op": "÷",
        "b": b,
        "answer": answer,
        "answer_type": "dec",
        "q_type": "normal",
    }


#5年生, 分数の足し算
def subject_5003(difficulty: int):
    #難易度調整
    value   = value_each_difficulty(difficulty, 9, 18, 20)		#分母
    value2 = value_each_difficulty(difficulty, 9, 18, 20)		#分子
    if value == -1 or value2 == -1:
        return -1, "error", -1, -1, -1

    #分母を決める
    a = random.randint(2,value)	#分母(前)
    b = random.randint(1, value2)	#分母(後)

    #分子を決める
    c = random.randint(2,value)	#分母(前)
    d = random.randint(1, value2)	#分母(後)

    #答えを算出する
    e = Fraction(c,a)
    f = Fraction(d,b)
    answer = e + f

    return {
        "a": e,
        "op": "＋",
        "b": f,
        "answer": answer,
        "answer_type": "fra",
        "q_type": "normal",
    }


#5年生, 分数の引き算
def subject_5004(difficulty: int):
    #難易度調整
    value   = value_each_difficulty(difficulty, 9, 18, 20)		#分母
    value2 = value_each_difficulty(difficulty, 9, 18, 20)		#分子
    if value == -1 or value2 == -1:
        return -1, "error", -1, -1, -1

    #分母を決める
    a = random.randint(2,value)	#分母(前)
    b = random.randint(1, value2)	#分母(後)

    #分子を決める
    c = random.randint(2,value)	#分母(前)
    d = random.randint(1, value2)	#分母(後)

    #分数生成
    e = Fraction(c,a)
    f = Fraction(d,b)

    #答えが負になったらe,fを入れ替える
    if e < f:
        e,f = f,e

    #答えを算出する
    answer = e - f

    return {
        "a": e,
        "op": "-",
        "b": f,
        "answer": answer,
        "answer_type": "fra",
        "q_type": "normal",
    }
