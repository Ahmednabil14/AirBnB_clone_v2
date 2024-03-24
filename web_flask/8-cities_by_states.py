#!/usr/bin/python3
"""List of states"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def states_list():
    """list states"""
    states = storage.all(State).values()
    # sorted return a new list
    sorted_states = sorted(states, key=lambda x: x.name)
    for state in sorted_states:
        # sort change in the list
        state.cities.sort(key=lambda city: city.name)
    return render_template(
        "8-cities_by_states.html", sorted_states=sorted_states)


@app.teardown_appcontext
def close_sqlalchemy_session(exception=None):
    """closing sqlalchemy session after each request to reload"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
