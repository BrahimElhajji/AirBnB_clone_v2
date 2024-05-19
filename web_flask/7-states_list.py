#!/usr/bin/python3
"""Import Flask for runing the web app"""
from flask import Flask, render_template
from models import storage
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import request, abort

app = Flask(__name__)


engine = create_engine('sqlite:///storage.db')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))


@app.teardown_appcontext
def teardown_db_session(exception):
    """teardown the database session after each request"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """route to display the list of states"""
    states = storage.all("State")
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
