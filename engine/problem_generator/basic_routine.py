from fractions import Fraction
import random


#難易度に応じて、出題する問題の数を大きく調整するための関数
def value_each_difficulty(difficulty: int, easy_v: int, normal_v: int, hard_v: int):
    value = -1

    match difficulty:
        case 1:
            value = easy_v
        case 2:
            value = normal_v
        case 3:
            value = hard_v
        case _:
            value = -1

    return value


#答えの型に応じて4択生成アルゴリズムを分岐させる関数
def generate_choices(answer, answer_type):

    if answer_type == "int":
        return generate_int_choices(answer)

    elif answer_type == "fraction":
        return generate_fraction_choices(answer)

    elif answer_type == "decimal":
        return generate_decimal_choices(answer)


#答えがint型の場合の4択生成アルゴリズム
def generate_int_choices(answer):

    choices = {answer}

    while len(choices) < 4:

        delta = random.choice([-3,-2,-1,1,2,3,5,10])
        wrong = answer + delta

        if wrong >= 0:
            choices.add(wrong)

    choices = list(choices)
    random.shuffle(choices)

    return choices


#答えがfloat型の場合の4択生成アルゴリズム
def generate_decimal_choices(answer):

    choices = {answer}

    while len(choices) < 4:

        delta = random.choice([-0.3,-0.2,-0.1,0.1,0.2,0.3])
        wrong = round(answer + delta, 2)

        if wrong >= 0:
            choices.add(wrong)

    choices = list(choices)
    random.shuffle(choices)

    return choices


#答えが分数型の場合の4択生成アルゴリズム
def generate_fraction_choices(answer):

    choices = {answer}

    while len(choices) < 4:

        delta_num = random.choice([-2,-1,1,2])
        wrong = answer + Fraction(delta_num, answer.denominator)

        if wrong > 0:
            choices.add(wrong)

    choices = list(choices)
    random.shuffle(choices)

    return choices


#表示用フォーマット
def fraction_to_string(frac):
    return f"{frac.numerator}/{frac.denominator}"