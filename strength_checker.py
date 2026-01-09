import re

def password_strength(password):
    score = 0

    length = len(password)

    if 8 <= length <= 16:
        score += 1
    elif 17 <= length <= 19:
        score += 2
    elif length >= 19:
        score += 3


    if re.search(r"(?=.*[a-z]).*", password):
        score += 1
    if re.search(r"(?=.*[A-Z]).*", password):
        score += 1
    if re.search(  r"(?=.*[0-9]).*", password):
        score += 1
    if re.search(r"(?=.*[!@#$%^&*]).*", password):
        score += 1

    return score


UserInput = "password123"
