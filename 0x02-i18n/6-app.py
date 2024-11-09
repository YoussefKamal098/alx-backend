#!/usr/bin/env python3
"""A simple flask i18n app"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    """
    Setting the languages and the locale and timezone
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False

babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Selects the best matching language from the request headers.
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    if g.user:
        locale = g.user.get('locale')
        if locale in app.config['LANGUAGES']:
            return locale

    locale = request.headers.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """
    Returns a user dictionary or None if the ID cannot be found or
    if the user has no locale set.
    """
    user_id = int(request.args.get('login_as', -1))
    return users.get(user_id, None)


@app.before_request
def before_request():
    """
    Finds a user if any, and sets the locale and timezone for the request.
    """
    g.user = get_user()


@app.route('/')
def index() -> str:
    """ Renders an index.html template """
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
