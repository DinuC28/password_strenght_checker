from flask import Flask, render_template, request, redirect, url_for
from strength_checker import password_validation, password_strength
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/check_password', methods=['POST'])
def check_password():

    password = request.form['password']

    validation, feedback_messages = password_validation(password)

    score = password_strength(password)

    checked = f'<h3>Strength Score: {score}/15</h3>'

    for message in feedback_messages:
        checked += f'<div class = ""feedback>{message}</div>'


    return render_template('index.html', checked=checked)


if __name__ == "__main__":
    app.run(debug=True)


