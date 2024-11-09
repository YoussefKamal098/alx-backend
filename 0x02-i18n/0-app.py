#!/usr/bin/env python3
from flask import Flask, render_template

app = Flask(__name__)
app.strict_slashes = False


@app.route('/')
def index() -> str:
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
