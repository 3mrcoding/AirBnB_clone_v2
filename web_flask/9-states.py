#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_list():
    """states list"""
    states = storage.all("State")
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_list_id(id):
    """states list"""
    states = storage.all("State")
    state = states.get(id)
    for state in storage.all("State").values():
        if state.id == id:
            return render_template('9-states.html', states=states, state=state,
                                   id=id, NoID=False)
    return render_template('9-states.html', NoID=True)


@app.teardown_appcontext
def terminate(exc):
    """Close SQLAlchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
