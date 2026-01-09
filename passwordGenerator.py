import string
import secrets

default_length = 16
default_chars = string.ascii_letters + string.digits + string.punctuation

CHAR_POOL = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+[]{};:'\",./?`~"

def generate_password(length=default_length):
    if length < 8:
        length = default_length
    password = []
    for i in range(length):
        password.append(secrets.choice(CHAR_POOL))
    return ''.join(password)

