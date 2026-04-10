import re

def password_strength(password):

    score = 0
    length = len(password)
    score_messages = []


    #check the length of the password
    if length < 8:
        score += 0
        score_messages.append("The password is too short")

    elif length == 8:
        score_messages.append("The password can be longer")
        score += 1

    elif length <= 16:
        score_messages.append("The length of the password is average")
        score += 2

    elif length <= 20:
        score_messages.append("The length of the password is really good")
        score += 3

    elif length > 20:
        score_messages.append("The length of the password is above average")
        score += 4


    #checking character variety using regex
    #checking for lower case letters
    """
    Max O'Didily (2023). Check the Strength of a Password Using Python. [online] YouTube. Available at: https://www.youtube.com/watch?v=oPZJxF1a8o8&list=PLrqwM2iFagujzmtufjj0lbCVvmyattGLc&index=3 [Accessed 9 Apr. 2026].
    Note: The YouTube tutorial was used for the regex logic 
‌
    """
    if re.search(r"(?=.*[a-z]).*", password):
        score += 2
    else:
        score -= 1
        score_messages.append("The password is missing a lower case letter")

    #checking for upper case letters
    if re.search(r"(?=.*[A-Z]).*", password):
        score += 2
    else:
        score -= 1
        score_messages.append("The password is missing a upper case letter")

    #check for numbers
    if re.search(r"(?=.*[0-9]).*", password):
        score += 4
    else:
        score -= 2
        score_messages.append("The password is missing a number")

    #check for special characters
    if re.search(r"(?=.*[!@#$%^&*]).*", password):
        score += 4
    else:
        score -= 2
        score_messages.append("The password is missing a special character")



    #check the score of the password
    if score < 5:
        score_messages.append("The password is not strong enough")

    elif score <=10:
        score_messages.append("The password needs to be stronger")

    elif score <=15:
        score_messages.append("The password is strong")

    elif score > 15:
        score_messages.append("The password is really strong")


    #check if the score is under 0 and make it 0
    if score < 0:
        score = 0

    return score, score_messages


#checking for repeating characters
"""
Max O'Didily (2022). Checking for Repeating Characters in a Password Using Python - Simple Validation. [online] YouTube. Available at: https://www.youtube.com/watch?v=fr3SmErTlnI&list=PLrqwM2iFagujzmtufjj0lbCVvmyattGLc&index=2 [Accessed 8 January. 2026].
Note: The repeating character function was implemented from the YouTube tutorial
‌
"""
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


#check if all the characters in the password are digits
"""
Max O'Didily (2023). Python Password Validation: Checking if a Password Contains Only Digits. [online] YouTube. Available at: https://www.youtube.com/watch?v=yOduH7xXpCw&list=PLrqwM2iFagujzmtufjj0lbCVvmyattGLc&index=4 [Accessed 10 Apr. 2026].
Note: The function to check if all the characters in the password are digits was implemented from the YouTube tutorial
‌
"""
def is_all_digits(password):
    return password.isdigit()

#check if the password meets the length requirement
def has_valid_length(password):
    return 8 <= len(password) <= 64

#check if the password meets all the validation checks and gives feedback back to the user
def password_validation(password):

    feedback_messages = []

    valid_length = has_valid_length(password)
    all_digits = is_all_digits(password)
    has_repeats = repeating_character(password, 3)
    has_sequence = sequence_checking(password, 3)
    has_pattern = checking_patterns(password, 3)

    if not valid_length:
        feedback_messages.append("The length of the password needs to be 8 characters or more")
    else:
        feedback_messages.append("The password length meets the length requirement")

    if all_digits:
        feedback_messages.append("The password needs to include more than digits")
    else:
        feedback_messages.append("The password includes more than digits")

    if not has_repeats:
        feedback_messages.append("The characters in the password cannot repeat more than 3 times")

    if has_sequence:
        feedback_messages.append("The password cannot include a sequence of characters")

    if has_pattern:
        feedback_messages.append("The password includes a common keyboard pattern:")


    validation = (
            password != "" and
            valid_length and
            has_repeats and
            has_sequence and
            not has_pattern and
            not all_digits
    )

    return validation, feedback_messages


"""
Note: Google Gemini was used to debug this function
Google (2026) Gemini [Large language model]. Available at: https://gemini.google.com (Accessed: 28/January/2026)
"""
def checking_patterns(password, min_sequence = 3):

    password = password.lower()

    qwerty_keyboard = [
        #common horizontal qwerty keyboard patterns
        '1234567890-=',
        'qwertyuiop[]',
        'asdfghjkl;"',
        'zxcvbnm,./',

        #common vertical qwerty keyboard patterns
        "1qaz",
        "2wsx",
        "3edc",
        "4rfv",
        "5tgb",
        "6yhn",
        "7ujm",
        "8ik,",
        "9ol.",
        "0p;/"
    ]

    found_patterns = False

    for pattern in qwerty_keyboard:
        for i in range(len(pattern) - min_sequence + 1):

            forward_pattern = pattern[i:i + min_sequence]
            backward_pattern = forward_pattern[:: - 1]

            if forward_pattern in password or backward_pattern in password:
                found_patterns = True

    return found_patterns


"""
Note: Google Gemini was used to debug the function below. The implementation is my original idea as well as the logic behind the function
Google (2026) Gemini [Large language model]. Available at: https://gemini.google.com (Accessed: 31/January/2026)
"""
def sequence_checking(password, min_sequence = 3):
    for i in range(len(password) - min_sequence + 1):
        sequence = password[i:i + min_sequence]

        is_accending = all(ord(sequence[j]) == ord(sequence[j - 1]) + 1 for j in range(1, len(sequence)))

        is_deccending = all(ord(sequence[j]) == ord(sequence[j - 1]) - 1 for j in range(1, len(sequence)))

        if is_accending or is_deccending:
            return True

    return False

