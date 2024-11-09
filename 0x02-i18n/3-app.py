#!/usr/bin/env python3
"""A simple flask i18n app"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """
    Setting the languages and the locale and timezone
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False

babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Selects the best matching language from the request headers.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """ Renders an index.html template """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
