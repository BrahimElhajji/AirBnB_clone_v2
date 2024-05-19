#!/usr/bin/python3
"""starting a Flask web application"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """fun that display HBNB"""
    return "HBNB"


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """fun that display Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """fun that display C followed by the value of the text variable"""
    text = text.replace("_", " ")
    return "C " + text


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", strict_slashes=False)
def python_text(text="is cool"):
    """fun that display Python followed by the value of the text variable"""
    text = text.replace("_", " ")
    return "Python " + text


@app.route("/number/<int:n>", strict_slashes=False)
def number_n(n):
    """fun that display n is a number only if n is an integer"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template_n(n):
    """fun that display a HTML page only if n is an integer"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even_n(n):
    """fun that display a HTML page only if n is an integer:
    H1 tag: Number: n is even|odd” inside the tag BODY"""
    if n % 2 == 0:
        status = "even"
    else:
        status = "odd"
    return render_template("6-number_odd_or_even.html", n=n, status=status)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
