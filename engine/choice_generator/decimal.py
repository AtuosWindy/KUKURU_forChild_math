import random

def generate(answer):

    choices = set([answer])

    while len(choices) < 4:
        d = random.randint(1,3)

        choices.add(max(0, answer + round(random.randrange(-0.5,0.5), d)))

    choices = list(choices)

    return choices