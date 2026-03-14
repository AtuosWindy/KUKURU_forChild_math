import random
from fractions import Fraction

def generate(answer):

    choices = set([answer])

    while len(choices) < 4:

        n = answer.numerator + random.choice([-2,-1,1,2])
        d = answer.denominator

        if n > 0:
            frac = Fraction(n, d)
            choices.add(frac)

    return list(choices)