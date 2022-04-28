#!/usr/bin/python3
"""
Starts a flask web application
"""
from flask import Flask, render_template
from models.state import State
from models import storage, storage_type

app = Flask(__name__)


@app.teardown_appcontext
def close_session(self):
    """removes the current SQLAlchemy Session"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def display_cities():
    """displays a html page with state cities"""
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
