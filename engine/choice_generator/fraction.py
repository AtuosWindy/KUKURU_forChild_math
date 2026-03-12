import random
from fractions import Fraction

def generate(answer):

    choices = set([answer])

    while len(choices) < 4:
        n = answer.numerator + random.choice([-1, 1])
        d = answer.denominator + random.choice([-1, 1])

        if n > 0 and d > 0:
            frac = Fraction(n, d)
            choices.add(frac)

    choices = list(choices)

    return choices