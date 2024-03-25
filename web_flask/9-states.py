#!/usr/bin/python3
"""List of states"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states_list():
    """list states"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda x: x.name)
    return render_template("7-states_list.html", sorted_states=sorted_states)


@app.route("/states/<id>", strict_slashes=False)
def cities_list(id):
    """list all cities in this state"""
    states = storage.all(State).values()
    for state in states:
        if id == state.id:
            state.cities.sort(key=lambda city: city.name)
            return render_template(
                "9-states.html",
                state=state.name,
                cities=state.cities,
                find=True)
    return render_template("9-states.html", find=False)


@app.teardown_appcontext
def close_sqlalchemy_session(exception=None):
    """closing sqlalchemy session after each request to reload"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
