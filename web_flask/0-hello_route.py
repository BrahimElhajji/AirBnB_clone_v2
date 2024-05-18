#!/usr/bin/python3
"""starting a Flask web application"""
from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_hbnb():
    """fun that display Hello HBNB!"""
    return "<h1>Hello HBNB!</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
