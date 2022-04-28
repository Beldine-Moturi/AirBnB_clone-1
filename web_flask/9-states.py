#!/usr/bin/python3
"""Starts a Flask web application
fetches data from a database and displays it on a web page
"""
from models import storage
from flask import Flask, render_template
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states', strict_slashes=False)
def display_all_states():
    """Displays all states in the database"""
    return render_template('9-states.html', state=storage.all(State))


@app.route('/states/<id>', strict_slashes=False)
def display_states(id):
    """display a HTML page: (inside the tag BODY)"""
    for state in storage.all(State).values():
        if state.id == id:
            return render_template('9-states.html', state=state)
    return render_template('9-states.html')


@app.teardown_appcontext
def close_db_session(exception):
    """removes the current SQLAlchemy Session
    after each request"""
    storage.close()


if __name__ == "__main__":
    """run flask web app"""
    app.run(host='0.0.0.0')
