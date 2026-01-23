import re

def password_strength(password):

    score = 0
    length = len(password)

    if length < 6:
        score += 0
        print("The password is too short")

    elif length <= 8:
        score += 1
        print("The password can be longer")

    elif length <= 16:
        score += 2
        print("The length of the password is average")

    elif length <= 20:
        score += 3
        print("The password length exceeds 16 characters")

    elif length > 20:
        score += 4
        print("The length of the password is above average")

    if re.search(r"(?=.*[a-z]).*", password):
        score += 2
    else:
        score -=1
        print("The password is missing a lower case letter.")

    if re.search(r"(?=.*[A-Z]).*", password):
        score += 2
    else:
        score -=1
        print("The password is missing a upper case letter.")

    if re.search(r"(?=.*[0-9]).*", password):
        score += 2
    else:
        score -=1
        print("The password is missing a number")

    if re.search(r"(?=.*[!@#$%^&*]).*", password):
        score += 4
    else:
        score -= 2
        print("The password is missing a special character.")


    if score < 5:
        print("Password is too weak")

    elif score <= 10:
        print("The password needs to be stronger")

    elif score <= 15:
        print("The password is strong")

    elif score > 15:
        print("The password is really strong")

    if score < 0:
        return 0

    return score

def valid_length(password):
    return len(password) <= 8 and len(password) <= 16

def is_all_digits(password):
    return password.isdigit()

#checking for repeating characters
def repeating_character(password, maxRepeat):

    character_count = 0
    last_character = None

    for i in range(1, len(password)):
        last_character = password[i - 1]

        if password[i] == last_character:
            character_count += 1
        else:
            character_count = 0

        if character_count == maxRepeat:
            return False

    return True

#checking for sequence of characters
def checking_sequence(password, max_sequence_length):

    passwordValue = [ord(c) for c in password]

    for i in range(len(passwordValue) - max_sequence_length + 1):
        sequence = passwordValue[i:i + max_sequence_length]
        if(sequence == list(range(sequence[0], sequence[0] + max_sequence_length))
                or sequence == list(range(sequence[0], sequence[0] + max_sequence_length, -1))
        ):
            return False
    return True



print("Enter your password")
user_password = input()

