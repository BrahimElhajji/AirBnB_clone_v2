"""starting a Flask web application"""
from flask import Flask

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
