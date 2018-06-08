from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/cho")
def cho():
    return "Hello Ei Cho Zin"
