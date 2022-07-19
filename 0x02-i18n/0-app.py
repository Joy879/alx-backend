#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    """Returns a simple html page"""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run()
