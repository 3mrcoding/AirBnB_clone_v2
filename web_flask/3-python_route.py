#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """/c/<text>"""
    text_new = text.replace('_', ' ')
    return f'C {escape(text_new)}'


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def py_text(text='is cool'):
    """/python/<text>"""
    text_new = text.replace('_', ' ')
    return f'Python {escape(text_new)}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
