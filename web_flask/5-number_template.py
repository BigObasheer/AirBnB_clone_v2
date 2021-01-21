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
    """ Display C followed by value of text variable """
    return ("C {}".format(text.replace("_", " ")))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python(text="is cool"):
    """ Display Python followed by value of text """
    if (text == "is cool"):
        return("Python {}".format(text))
    else:
        return("Python {}".format(text.replace("_", " ")))


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """ Display number only if n is an int """
    return("{} is a number".format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_html(n):
    """ Display html page only if n is an int """
    return render_template('5-number.html', n=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
