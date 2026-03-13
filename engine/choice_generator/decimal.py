import random

def generate(answer):

    choices = set([answer])

    while len(choices) < 4:
        dig = 3
        if int(answer * 10) == answer * 10:
            dig = 1
        elif int(answer * 100) == answer * 100:
            dig = 2

        choices.add(max(0, answer + round(random.uniform(-0.5,0.5), dig)))

    choices = list(choices)

    return choices