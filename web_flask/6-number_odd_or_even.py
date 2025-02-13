#!/usr/bin/python3
"""
Starts a minimal flask application
listening on 0.0.0.0:5000
Routes:
    / - display "Hello HBNB!"
    /hbnb - display "HBNB"
    /c/<text> - display "C <text>"
"""
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """Displays Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """Displays HBNB"""
    return "HBNB"


@app.route('/c/<string:text>')
def display_text(text):
    """Displays C followed by the input parameter <text>"""
    new_text = text.replace("_", " ")
    return "C %s" % new_text


@app.route('/python')
@app.route('/python/<string:text>')
def display_python(text="is cool"):
    """ Displays python followed by the input parameter <text>"""
    new_text = text.replace("_", " ")
    return "Python %s" % new_text


@app.route('/number/<int:n>')
def number_route(n):
    """Displays <n> followed by 'is a number'"""
    return "%i is a number" % n


@app.route('/number_template/<int:n>')
def number_template(n):
    """Displays a html page"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """Displays a html template"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
