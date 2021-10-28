from flask import Flask, g, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("base.html")
def hello():
    return render_template("hello.html")

@app.route("/submit/", methods = ["POST", "GET"])
def submit():
    if request.method == "POST":
        return render_template("submit.html")
    else:
        try:
            return render_template("submit.html")
        except:
            return render_template("submit.html")
