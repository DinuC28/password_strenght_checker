from flask import Flask, render_template, request, redirect, url_for
from strength_checker import password_validation
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/password_checker', methods=['POST'])
def check_password():
    password = request.form.get('password')
    checked = password_validation(password)
    return render_template('index.html', checked = checked)


if __name__ == "__main__":
    app.run(debug=True)


