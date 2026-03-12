import random
import math
from fractions import Fraction
from .basic_routine import value_each_difficulty


#difficulty - 1(かんたん)~3(むずかしい)

#文字式（簡単な式 ー 足し算）／例 : x(answer) + 3(a) = 7(b) とか。answer2: xと3の順番
def x_add(value, value2):
    b = random.randint(1,value2)
    a = random.randint(1,b)
    answer = b - a
    answer2 = random.randint(0,1)		#0でx + 3 = ~("left_op")、1で 3 + x = ~("right_op") ...
    q_type = "left_op"		#normalな形ではない("="の左側ではある)けど、opの左(left)に"?"が位置する
    if answer2 == 1:
        q_type = "right_op"		#normalな形ではない("="の左側ではある)けど、opの右(right)に"?"が位置する

    return {
        "a": a,
        "op": "+",
        "b": b,
        "answer": answer,
        "answer_type": "int",
        "q_type": q_type,
    }
    
#文字式（簡単な式 ー 引き算）／例 : x(answer) - 3(a) = 7(b) とか。answer2: xと3の順番
def x_sub(value, value2):
    answer2 = random.randint(0,1)		#0でx - 3 = ~、1で 3 - x = ~ ...
    a = 0
    b = 0
    q_type = None

    if answer2 == 0:
        a = random.randint(1, value)
        b = random.randint(1, value2)
        answer = a + b
        q_type = "left_op"		#normalな形ではない("="の左側ではある)けど、opの左(left)に"?"が位置する
    else:
        b = random.randint(1, value2)
        a = random.randint(b, value)
        answer = a - b
        q_type = "right_op"		#normalな形ではない("="の左側ではある)けど、opの右(right)に"?"が位置する

    return {
        "a": a,
        "op": "-",
        "b": b,
        "answer": answer,
        "answer_type": "int",
        "q_type": q_type,
    }

#文字式（簡単な式 ー かけ算）／例 : x(answer) × 3(a) = 12(b) とか。answer2: xと3の順番
def x_mul(value, value2):
    a = random.randint(1, value)
    answer = random.randint(1, value2)
    b = a * answer
    answer2 = random.randint(0,1)		#0で x × 3 = ~、1で 3 × x = ~ ...
    q_type = "left_op"		#normalな形ではない("="の左側ではある)けど、opの左(left)に"?"が位置する
    if answer2 == 1:
        q_type = "right_op"		#normalな形ではない("="の左側ではある)けど、opの右(right)に"?"が位置する

    return {
        "a": a,
        "op": "×",
        "b": b,
        "answer": answer,
        "answer_type": "int",
        "q_type": q_type,
    }

#文字式（簡単な式 ー 割り算）／例 : x(answer) ÷ 3(a) = 12(b) とか。answer2: xと3と12の順番
#answer2が0→x÷3=12, 1→12÷x=3
def x_div(value, value2):
    a = random.randint(1, value)
    answer = random.randint(1, value2)
    b = a * answer
    answer2 = random.randint(0,1)		#0で x÷3 = ~、1で 12÷x = ~ ...(xが4の場合)

    q_type = "left_op"		#normalな形ではない("="の左側ではある)けど、opの左(left)に"?"が位置する
    if answer2 == 1:
        q_type = "right_op"		#normalな形ではない("="の左側ではある)けど、opの右(right)に"?"が位置する
        a,b = b,a

    return {
        "a": a,
        "op": "÷",
        "b": b,
        "answer": answer,
        "answer_type": "int",
        "q_type": q_type,
    }


#6年生, 分数 × 分数
def subject_6001(difficulty: int):
    #難易度調整
    value   = value_each_difficulty(difficulty, 9, 18, 20)		#分母
    value2 = value_each_difficulty(difficulty, 9, 18, 20)		#分子
    if value == -1 or value2 == -1:
        return -1, "error", -1, -1, -1

    #分母を決める
    a = random.randint(2,value)	#分母(前)
    b = random.randint(2,value)	#分母(後)

    #分子を決める
    c = random.randint(2,value2)	#分子(前)
    d = random.randint(2,value2)	#分子(後)

    #答えを算出する
    e = Fraction(c,a)
    f = Fraction(d,b)
    answer   = e * f

    return {
        "a": e,
        "op": "×",
        "b": f,
        "answer": answer,
        "answer_type": "fra",
        "q_type": "normal",
    }


#6年生, 分数 ÷ 分数
def subject_6002(difficulty: int):
    #難易度調整
    value   = value_each_difficulty(difficulty, 9, 18, 20)		#分母
    value2 = value_each_difficulty(difficulty, 9, 18, 20)		#分子
    if value == -1 or value2 == -1:
        return -1, "error", -1, -1, -1

    #分母を決める
    a = random.randint(2,value)	#分母(前)
    b = random.randint(2,value)	#分母(後)

    #分子を決める
    c = random.randint(2,value2)	#分子(前)
    d = random.randint(2,value2)	#分子(後)

    #答えを算出する
    e = Fraction(c,a)
    f = Fraction(d,b)
    answer = e / f

    return {
        "a": e,
        "op": "÷",
        "b": f,
        "answer": answer,
        "answer_type": "fra",
        "q_type": "normal",
    }


#6年生, 文字式（簡単な式）／例：x(answer) +(op) 3(a) = 7(b)とか(answer2: xと3の順序...値は0と1にするか..)
def subject_6003(difficulty: int):
    #難易度調整
    value   = value_each_difficulty(difficulty, 9, 9, 20)		#aの範囲用
    value2 = value_each_difficulty(difficulty, 9, 9, 20)		#bの範囲用
    op = "+"
    if difficulty == 3 or difficulty == 2:
        op = random.choice(["+", "-", "×", "÷"])
    elif difficulty == 2:
        op = random.choice(["+", "-", "×"])
    else:
        op = random.choice(["+", "-"])

    if op == "+":
        return x_add(value, value2)
    elif op == "-":
        return x_sub(value, value2)
    elif op == "-":
        return x_mul(value, value2)
    elif op == "÷":
        return x_div(value, value2)


#6年生, エキストラ問題
def subject_6004(difficulty: int):
    #難易度調整は、6004だけは常にMAX想定。”エキストラ”だからね。
    #これまでのすべての問題の組み合わせで完全ランダムを想定。
    #ここだけはちょっと特殊になりそうなので一旦後回し。
    return {
        "a": 0,
        "op": "+",
        "b": 0,
        "answer": 0,
        "answer_type": "int",
        "q_type": "normal",
    }
