def password_length(password):

    if len(password) >= 8 or len(password) <= 0:

        lowerCase = False
        upperCase = False
        character = False
        number = False

        for char in password:
            if char.islower():
                return True
            if char.isupper():
                return True
            if char.isdigit():
                return True
            if not char.islnum():
                return True

        return False
    else:
        return True

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


def digitChecker(password):
    return password.isdigit()


UserInput = "Dinu123!"

print(password_length(UserInput))
print(repeating_character(UserInput, 2))