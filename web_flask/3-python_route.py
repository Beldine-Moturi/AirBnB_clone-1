#!/usr/bin/python3
"""
Starts a minimal flask application
listening on 0.0.0.0:5000
Routes:
    / - display "Hello HBNB!"
    /hbnb - display "HBNB"
    /c/<text> - display "C <text>"
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays HBNB"""
    return "HBNB"


@app.route('/c/<string:text>', strict_slashes=False)
def display_text(text):
    """Displays C followed by the input parameter <text>"""
    new_text = text.replace("_", " ")
    return "C %s" % new_text


@app.route('/python', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def display_python(text="is cool"):
    """ Displays python followed by the input parameter <text>"""
    new_text = text.replace("_", " ")
    return "Python %s" % new_text


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
