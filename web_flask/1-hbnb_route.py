#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    """Hello HBNB!"""
    return 'Hello HBNB!'

@app.route('/hbnb')
def hello_hbnb():
    """HBNB"""
    return 'HBNB'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
