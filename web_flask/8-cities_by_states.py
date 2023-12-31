#!/usr/bin/python3
"""
    Started a Flask web application with these scripts
    the web apps was listed on 0.0.0.0, port 5000
    declare @app.teardown_appcontext and storage.close()
    with routes /cities_by_states: display a HTML page:
    in my route def option strict_slashes=False was used
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from operator import getitem
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_states():
    """List all the states to the client"""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states', strict_slashes=False)
def list_states_cities():
    """List all the states and its cities to the client"""
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def close_db(db):
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
