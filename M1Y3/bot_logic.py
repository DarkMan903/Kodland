import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password

def games():
    flip = random.randint(0,2)
    if flip == 0:
        return "Орел"
    else:
        return "Решка"

def emojes():
    emojess = [":heart:", ":sparkles:", ":joy:", ":smiling_face_with_tear:"]
    return random.choice(emojess)