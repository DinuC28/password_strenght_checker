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

    elif length <= 16:
        score += 2

    elif length <= 20:
        score += 3

    elif length > 20:
        score += 4


    #checking for lower case letters
    if re.search(r"(?=.*[a-z]).*", password):
        score += 2
    else:
        score -= 1
        print("The password is missing a lower case letter")

    #checking for upper case letters
    if re.search(r"(?=.*[A-Z]).*", password):
        score += 2
    else:
        score -= 1
        print("The password is missing a upper case letter")

    #check for numbers
    if re.search(r"(?=.*[0-9]).*", password):
        score += 4
    else:
        score -= 2
        print("The password is missing a number")

    #check for special characters
    if re.search(r"(?=.*[!@#$%^&*]).*", password):
        score += 4
    else:
        score -= 2
        print("The password is missing a special character")


    #check the score of the password
    if score < 5:
        print("The password is not strong enough")

    elif score <=10:
        print("The password needs to be stronger")

    elif score <=15:
        print("The password is strong")

    elif score > 15:
        print("The password is really strong")


    #check if the score is under 0 and make it 0
    if score < 0:
        return 0

    return score


UserInput = "Dinu2873@!£42686848"
print(password_strength(UserInput))