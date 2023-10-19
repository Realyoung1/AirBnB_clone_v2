#!/usr/bin/python3
"""
    Started a Flask web application with these scripts
    the web apps was listed on 0.0.0.0, port 5000
    with routes /: display “Hello HBNB!”
    in my route def option strict_slashes=False was used
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """Say hello to the client"""
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
