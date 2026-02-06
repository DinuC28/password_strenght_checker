from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")
    elif request.method == 'POST':
        return ""
    return None


if __name__ == "__main__":
    app.run(debug=True)


