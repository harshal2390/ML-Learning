from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def welcome():
    return render_template("index.html")

@app.route("/home")
def home():
    return "welcome to home"


if __name__=="__main__":
    app.run(debug=True)
