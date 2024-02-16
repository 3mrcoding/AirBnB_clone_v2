#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def hello():
    """Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello_hbnb():
    """HBNB"""
    return 'HBNB'


@app.route('/c/<text>')
def c_text(text):
    """/c/<text>"""
    text_new = text.replace('_', ' ')
    return f'C {escape(text_new)}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
