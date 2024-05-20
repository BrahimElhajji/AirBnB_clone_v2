#!/usr/bin/python3
"""Import Flask for runing the web app"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """Displays a html page with states"""
    states = storage.all('State')
    sorted_states = sorted(states, key=lambda x: x.name)
    return render_template('9-states.html', states=sorted_states)


@app.route('/states/<string:id>', strict_slashes=False)
def state(id):
    """Displays a html page with citys of that state"""
    state = storage.get('State', id)
    if state:
        return render_template('9-states.html', state=state)
    else:
        return render_template('not_found.html')


@app.teardown_appcontext
def close_storage(exc):
    """close the session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
