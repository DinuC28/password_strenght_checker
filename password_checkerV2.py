import re

def password_strength(password):

    score = 0
    length = len(password)

    #check the length of the password
    if length < 6:
        score += 0
        print("The password is too short")

    elif length <= 8:
        score += 1
        print("The password can be longer ")

    elif length <= 16:
        score += 2
        print("The length of the password is average")

    elif length <= 20:
        score += 3
        print("The length of the password is really good")
    else:
        score += 4
        print("The length of the password is above average")



    if re.search("[a-z]", password):
        score += 2
    else:
        score -= 1
        print("The password is missing a lower case letter")

    if re.search("[A-Z]", password):
        score += 2
    else:
        score -= 1
        print("The password is missing a upper case letter")

    if re.search("[0-9]", password):
        score += 2
    else:
        score -= 1
        print("The password is missing a number")

    if re.search(r"(?=.*[!@#$%^&*]).*", password):
        score += 4
    else:
        score -= 2
        print("The password is missing a special character")

    if score < 5:
        print("Your password is not strong enough")

    elif score <= 10:
        print("Your password needs to be stronger")

    elif score <= 15:
        print("Your password is strong")

    elif score > 15:
        print("Your password is really strong and secure")


def has_all_digits(password):
    return password.isdigit()

