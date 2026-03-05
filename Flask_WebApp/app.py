from flask import Flask, render_template, request
from strength_checker import password_validation, password_strength
import hashlib
import base64
import uuid
import os
pepper = os.environ.get("PEPPERING_VALUE", "peppered_password")
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/check_password', methods=['POST'])
def check_password():

    file_path = "used_passwords.txt"
    password = request.form['password']

    with open('rockyou.txt', encoding = 'latin-1') as file:
        common_password = [line.strip() for line in file.readlines()]

    if password.lower() in common_password:
        checked = '<div class = "feedback error">This password has been found in a common password list</div>'
        return render_template('index.html', checked = checked)

    with open(file_path, "r") as file:
        used_password = file.read().splitlines()

    for entry in used_password:
        if ':' not in entry:
            continue
        salted_password, stored_hash = entry.split(':', 1)
        hashing = hashlib.sha256()
        hashing.update(password.encode() + salted_password.encode() + pepper.encode())
        check_hash = base64.b64encode(hashing.digest()).decode()

        if check_hash == stored_hash:
            checked = '<h3>This password has already been used</h3>'
            checked += '<div class = "feedback error">Please enter a different password.</div>'
            return render_template('index.html', checked = checked)

    salt = base64.urlsafe_b64encode(uuid.uuid4().bytes).decode()
    hashing = hashlib.sha256()
    hashing.update(password.encode() + salt.encode() + pepper.encode())
    hashed_password = base64.b64encode(hashing.digest()).decode()

    with open(file_path, "a") as file:
        file.write(salt + ':' + hashed_password + '\n')


    validation, feedback_messages = password_validation(password)
    score, strength_feedback = password_strength(password)

    checked = f'<h3>Strength Score: {score}/15</h3>'
    checked += '<h4>Strength Analysis:</h4>'

    for message in strength_feedback:
        checked += f'<div class = "feedback">{message}</div>'

    checked += '<h4>Validation Checks:</h4>'
    for message in feedback_messages:
        checked += f'<div class = "feedback">{message}</div>'


    return render_template('index.html', checked=checked)

if __name__ == "__main__":
    app.run(debug=True)


