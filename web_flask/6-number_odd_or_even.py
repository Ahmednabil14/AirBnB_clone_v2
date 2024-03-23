#!/usr/bin/python3
"""Python is cool!"""
from flask import Flask, render_template


web_app = Flask(__name__)


# strict_slashes=False for ignoring / when accessing route
@web_app.route("/", strict_slashes=False)
def home_page():
    "define home page"
    return ("Hello HBNB!")


@web_app.route("/hbnb", strict_slashes=False)
def hbnb():
    """define hbnb page"""
    return ("HBNB")


# <text> for passing variable
@web_app.route("/c/<text>", strict_slashes=False)
# should pass as argument with the same name
def pass_variable(text):
    """passing argument as variable"""
    text_without_underscore = text.replace("_", " ")
    return ("C {}".format(text_without_underscore))


@web_app.route("/python", strict_slashes=False)
def python_home():
    """python is cool"""
    return ("Python is cool")


@web_app.route("/python/<text>", strict_slashes=False)
def python_is_cool(text):
    """python is cool"""
    text_without_underscore = text.replace("_", " ")
    return ("Python {}".format(text_without_underscore))


@web_app.route("/number/<int:n>", strict_slashes=False)
def is_number(n):
    """n is int or not"""
    return ("{} is a number".format(n))


@web_app.route("/number_template/<int:n>", strict_slashes=False)
def open_html(n):
    """open html file"""
    return render_template("5-number.html", n=n)


@web_app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def is_even(n):
    """even or odd"""
    if n % 2 == 0:
        return render_template("6-number_odd_or_even.html", n=n, text="even")
    else:
        return render_template("6-number_odd_or_even.html", n=n, text="odd")


if __name__ == "__main__":
    web_app.run(host="0.0.0.0", port=5000, debug=True)
