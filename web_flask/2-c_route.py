#!/usr/bin/python3
""" Start a Flask web application """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def start_flask():
    """ Display Hello HBNB! """
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """ Display HBNB """
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """ Display c followed by value of text variable """
    return ("C {}".format(text.replace("_", " ")))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
