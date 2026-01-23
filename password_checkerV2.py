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

def password_validation(password):

    results = {
        'is_empty': password == "",
        'valid_length': valid_length(password),
        'is_not_all_digits': not is_all_digits(password),
        'repeating_character': repeating_character(password, 3),
        'checking_sequence': checking_sequence(password, 2),
    }

    is_valid = (not results['is_empty'] and
                results['valid_length'] and
                results['is_not_all_digits'] and
                results['repeating_character'] and
                results['checking_sequence']
                )

    return is_valid, results

def password_feedback(result):
    if result['is_empty']:
        print("The password is empty")
        return

    if not result['valid_length']:
        print("The length of the password must be 8 or 16 characters")
    else:
        print("The password meets the length requirement")

    if not result['is_not_all_digits']:
        print("The password must contain more characters than just digots")

    if not result['repeating_character']:
        print("The password must not have more than 3 repeating characters ")

    if not result['checking_sequence']:
        print("The password must not contain sequential characters ")


def password_length(password):
    if len(password) >= 8:
        if len(password) <= 16:

            lowerCase = False
            upperCase = False
            character = False
            number = False

            for char in password:

                if char.islower():
                    lowerCase = True

                if char.isupper():
                    upperCase = True

                if char.isdigit():
                    number = True

                if not char.isalnum():
                    character = True

            return lowerCase and upperCase and character and number
        else:
            return False
    else:
        return False

#Main function
print("Enter your password")
user_password = input()

is_valid, results = password_validation(user_password)
password_feedback(results)

while not is_valid:
    print("\nPlease reenter your password")
    user_password = input()

    is_valid, result = password_strength(user_password)
    password_feedback(result)

print(password_feedback(results))
print(password_strength(user_password))
