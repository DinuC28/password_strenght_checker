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

def has_valid_length(password):
    return 8 <= len(password) <= 16


#Main function
print("Enter your password")
UserInput = input()

password_length(UserInput)
is_all_digits(UserInput)
repeating_character(UserInput, 3)
checking_sequence(UserInput, 2)

if has_valid_length(UserInput) == False:
    print("The length of the password should be between 8 and 16 characters")
else:
    print("The password suits the length requirement of 8 characters or more ")

if is_all_digits(UserInput) == True:
    print("The password needs to include more than digits")
else:
    print("The password includes more than digits")

if repeating_character(UserInput, 3) == False:
    print("The characters in the password should not repeat more than 3 times")

if checking_sequence(UserInput, 2) == False:
    print("The password needs to have a variety of characters")

#validation checks for empty string, all digits, repeating characters, and sequence
while UserInput == "" or password_length(UserInput) == False or is_all_digits(UserInput) == True or repeating_character(UserInput, 3) == False or checking_sequence(UserInput, 2) == False:

    print("Please renter your password again")
    UserInput = input()

    password_length(UserInput)
    is_all_digits(UserInput)
    repeating_character(UserInput, 3)
    checking_sequence(UserInput, 2)



    if password_length(UserInput) == False:
        print("The length of the password does not suit the requirement of 8 characters or more")
    else:
        print("The password suits the length requirement of 8 characters or more ")

    if is_all_digits(UserInput) == True:
        print("The password needs to include more than digits")
    else:
        print("The password includes more than digits")

    if repeating_character(UserInput, 3) == False:
        print("The characters in the password should not repeat more than 3 times")

    if checking_sequence(UserInput, 2) == False:
        print("The password needs to have a variety of characters")


print(password_strength(UserInput))


