#!/usr/bin/python3
"""Python is cool!"""
from flask import Flask


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


@web_app.route("/number/<n>", strict_slashes=False)
def is_number(n):
    """n is int or not"""
    if n.isdigit():
        return ("{} is a number".format(n))


if __name__ == "__main__":
    web_app.run(host="0.0.0.0", port=5000, debug=True)
