import string

password = "helloWorld"

upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
special = any([1 if c in string.punctuation else 0 for c in password])
digits = any([1 if c in string.digits else 0 for c in password])

length = len(password)

score = 0

charcters = [upper_case, lower_case, special, digits]

if length > 8:
    score += 1
if length > 16:
    score += 1


print(f"Password length is {str(length)}, adding {str(score)} points.")