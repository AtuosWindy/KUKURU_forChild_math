import random

def format_rem(q, r):
    if r == 0:
        return f"{q}"
    else:
        return f"{q}あまり{r}"

def generate(answer):

    q = answer["q"]
    r = answer["r"]
    b = answer["b"]

    choices = {(q,r)}

    while len(choices) < 4:

        dq = random.choice([-1,1])
        dr = random.choice([-1,1])

        new_q = max(0, q + dq)
        new_r = max(0, r + dr)
        if new_r == b:
            new_r = b - 1 if b > 1 else 0

        choices.add((new_q,new_r))

    choices = list(choices)

    random.shuffle(choices)

    return [
        format_rem(c[0], c[1]) for c in choices
    ]