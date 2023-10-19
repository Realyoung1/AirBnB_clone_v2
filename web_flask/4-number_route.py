#!/usr/bin/python3
"""
    Started a Flask web application with these scripts
    the web apps was listed on 0.0.0.0, port 5000
    routes /: display “Hello HBNB!” /hbnb: display “HBNB”
    /c/<text>: display “C ” followed by the value of the text
    /python/<text>: display “Python ”, foll the value of text
    /python/(<text>): display “Python ”, foll by value of text
    in my route def option strict_slashes=False was used
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """Say Hello HBNB to the client"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """Say HBNB to the client"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_isfun(text):
    """Say C and a given text to the client"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_iscool(text='is cool'):
    """Say Python and a given text to the client"""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def n_isnumber(n):
    """Say the number given in n to the client"""
    return '{} is a number'.format(n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
