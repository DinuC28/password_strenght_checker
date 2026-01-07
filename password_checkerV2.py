def password_length(password):

    if len(password) >= 8 or len(password) <= 0:

        lowerCase = False
        upperCase = False
        character = False
        number = False

        for char in password:
            if(char.islower()):
                lowerCase = True
            if(char.isupper()):
                upperCase = True
            if(char.isdigit()):
                number = True
            if(not char.islnum()):
                character = True

        return False
    else:
        return True


UserInput = "Dinu123!"

print(password_length(UserInput))