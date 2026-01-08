import re

def password_strength(password):
    score = 0

    length = len(password)

    if 8 <= length <= 16:
        score += 1
    if 16 <= length <= 32:

UserInput = "password123"
