import re

def password_strength(password):

    score = 0
    length = len(password)


    #check the length of the password
    if length < 6:
        score += 0
        print("The password is too short")

    elif length <= 8:
        print("The password can be longer")
        score += 1

    elif length <= 16:
        print("The length of the password is average")
        score += 2

    elif length <= 20:
        print("The length of the password is really good")
        score += 3

    elif length > 20:
        print("The length of the password is above average")
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


#check if all the characters in the password are digits
def is_all_digits(password):
    return password.isdigit()

#check if the password meets the length requirement
def has_valid_length(password):
    return 8 <= len(password) <= 16

#check if the password meets all the validation checks and gives feedback back to the user
def password_validation(password):

    valid_length = has_valid_length(password)
    all_digits = is_all_digits(password)
    has_repeats = repeating_character(password, 3)
    has_sequence = checking_sequence(password, 2)
    has_pattern = checking_patterns(password, 3)

    if not valid_length:
        print("The length of the password needs to be 8 characters or more")
    else:
        print("The password length meets the length requirement")

    if all_digits:
        print("The password needs to include more than digits")
    else:
        print("The password includes more than digits")

    if not has_repeats:
        print("The characters in the password cannot repeat more than 3 times")

    if not has_sequence:
        print("The password cannot include any sequence of characters")

    if has_pattern:
        print("The password includes a common keyboard pattern:")

    return (
        password != "" and
        valid_length and
        has_repeats and
        has_sequence and
        has_pattern
    )

def checking_patterns(password, min_sequence = 3):

    password = password.lower()

    patterns = [
        #common horizontal qwerty keyboard patterns
        '1234567890-=',
        'qwertyuiop[]',
        'asdfghjkl;"',
        'zxcvbnm,./'

        #common vertical qwerty keyboard patterns
        "1qaz",
        "2wsx",
        "3wxyz",
        "4rfv",
        "5tgb",
        "6yhn",
        "7ujm",
        "8ik,",
        "9ol.",
        "0p;/"
    ]

    matching_patterns = []

    for pattern in patterns:
        for i in range(len(pattern) - min_sequence + 1):
            forward = pattern[i:i + min_sequence]
            backward = forward[:: - 1]

            if forward in password:
                matching_patterns.append(forward)
            if backward in password:
                matching_patterns.append(backward)


    return list(set(matching_patterns))

#Main function
while True:
    password = input("Enter your password: ")
    if password_validation(password):
        break
    else:
        print("Please re-enter your password")

print(password_strength(password))


