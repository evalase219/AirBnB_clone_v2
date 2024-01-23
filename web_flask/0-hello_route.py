#!/usr/bin/python3
"""
Starts a Flash Web Application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    """ Prints a Message when / is called """
    return 'Hello HBNB!'


if __name__ == "__main__":
    """ Main Function """
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
