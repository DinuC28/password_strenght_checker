import re

def password_strength(password):

    score = 0
    length = len(password)


    if length < 8:
        score += 0
        print("The password is too short")

    elif 8 == length <= 16:
        score += 1
    elif 17 <= length <= 19:
        score += 2
    elif length >= 19:
        score += 3
    elif length == 20:
        score += 4
    elif length > 20:
        score += 5


    if re.search(r"(?=.*[a-z]).*", password):
        score += 1
    if re.search(r"(?=.*[A-Z]).*", password):
        score += 2
    if re.search(r"(?=.*[0-9]).*", password):
        score += 3
    if re.search(r"(?=.*[!@#$%^&*]).*", password):
        score += 4

    if score < 5:
        print("The password is not strong enough")
    elif score <= 5 or score < 9:
        print("The password needs to be stronger")
    elif score >= 10 or score <= 15:
        print("The password is secure")
    elif score > 15:
        print("The password is really strong")


    return score


UserInput = ""
print(password_strength(UserInput))