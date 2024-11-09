#!/usr/bin/env python3
"""A simple flask i18n app"""
from datetime import datetime
from functools import wraps
from typing import Callable

from flask import Flask, render_template, request, g
from flask_babel import Babel, format_datetime
import pytz


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


def validate_timezone(func: Callable[..., str]) -> Callable[..., str]:
    """
    Decorator to validate the timezone returned by the `get_timezone`
    function.
    Ensures the timezone is valid by checking it against the list of
    supported timezones in `pytz`. If the timezone is invalid,
    returns the default timezone.
    """
    @wraps(func)
    def decorated_function(*args, **kwargs) -> str:
        timezone = func(*args, **kwargs)

        try:
            return pytz.timezone(timezone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            return pytz.timezone(app.config['BABEL_DEFAULT_TIMEZONE']).zone

    return decorated_function


@babel.timezoneselector
@validate_timezone
def get_timezone() -> str:
    """
    Selects the timezone from the request, user, or defaults.
    """
    timezone = request.args.get('timezone')
    if timezone:
        return timezone

    if g.user:
        timezone = g.user.get('timezone')
        if timezone:
            return timezone

    return app.config['BABEL_DEFAULT_TIMEZONE']


def get_user():
    """
    Returns a user dictionary or None if the ID cannot be found or
    if the user has no locale set.
    """
    try:
        user_id = int(request.args.get('login_as', -1))
        return users.get(user_id, None)
    except ValueError:
        return None


@app.before_request
def before_request():
    """
    Finds a user if any, and sets the locale and timezone for the request.
    """
    g.user = get_user()
    g.time = format_datetime(datetime.now())


@app.route('/')
def index() -> str:
    """ Renders an index.html template """
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
