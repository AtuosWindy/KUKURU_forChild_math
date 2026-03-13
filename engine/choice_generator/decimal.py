import random

def generate(answer):

    choices = set([answer])

    dig = 3
    if int(answer * 10) == answer * 10:
        dig = 1
    elif int(answer * 100) == answer * 100:
        dig = 2

    while len(choices) < 4:

        wrong = round(answer + random.uniform(-0.5,0.5), dig)

        choices.add(max(0, wrong))

    return list(choices)