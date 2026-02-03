from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/", methods=["POST", "GET"])
def index():
    #send the password to the python file
    if request.method == "POST":
        current_password = request.form.get("password")
        
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)


