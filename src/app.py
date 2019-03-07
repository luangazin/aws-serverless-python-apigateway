# app.py
print("START")
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    print("HELLo")
    return "Hello World!"