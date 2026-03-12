import random

def generate(answer):

    choices = set([answer])

    while len(choices) < 4:

        choices.add(max(0, answer + random.randint(-3,3)))

    choices = list(choices)

    return choices