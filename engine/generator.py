import random
from engine.problem_generator.subject_map import SUBJECT_MAP
from engine.choice_generator import integer
from engine.choice_generator import decimal
from engine.choice_generator import remain
from engine.choice_generator import fraction


def generate_problem(grade: int, subject: int, difficulty: int):

print("DEBUG:", grade, subject, difficulty)

func = SUBJECT_MAP[grade * 1000 + subject]

p = func(difficulty)

a = p["a"]
op = p["op"]
b = p["b"]
answer = p["answer"]
answer_type = p["answer_type"]
q_type = p["q_type"]

print("answer_type =", answer_type)

if q_type == "normal":
question = f"{a} {op} {b} = ?"
elif q_type == "left_op":
question = f"? {op} {a} = {b}"
elif q_type == "right_op":
question = f"{a} {op} ? = {b}"

if answer_type == "int":
choices = integer.generate(answer)

elif answer_type == "dec":
choices = decimal.generate(answer)

elif answer_type == "rem":
choices = remain.generate(answer)

elif answer_type == "rem":

choices = remain.generate(answer)

q = answer["q"]
r = answer["r"]

if r == 0:
answer = f"{q}"
else:
answer = f"{q} あまり {r}"

elif answer_type == "fra":
choices = fraction.generate(answer)

else:
raise ValueError(f"Unknown answer_type: {answer_type}")

random.shuffle(choices)

return {
"question": question,
"choices": choices,
"answer": answer
}