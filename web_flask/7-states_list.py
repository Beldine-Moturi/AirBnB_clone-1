#!/usr/bin/python3
"""Starts a Flask web application
fetches data from a database and displays it on a web page
"""
from models import storage
from flask import Flask, render_template
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def display_states():
    """display a HTML page: (inside the tag BODY)"""
    states = storage.all(State)
    return render_template('7-states_list.html', states=states.values())


@app.teardown_appcontext
def close_db_session(exception):
    """removes the current SQLAlchemy Session
    after each request"""
    storage.close()

if __name__ == "__main__":
    """run flask web app"""
    app.run(host='0.0.0.0', port=5000)
