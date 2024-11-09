# Flask i18n Project

## Table of Contents

- [Introduction](#introduction)
- [Overview of i18n (Internationalization)](#overview-of-i18n-internationalization)
- [Requirements](#requirements)
- [Key Concepts](#key-concepts)
  - [Flask-Babel](#flask-babel)
  - [pytz](#pytz)
  - [i18n (Internationalization)](#i18n-internationalization)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
  - [Step 1: Install Dependencies](#step-1-install-dependencies)
  - [Step 2: Create the Flask Application](#step-2-create-the-flask-application)
  - [Step 3: Set Up Translations](#step-3-set-up-translations)
  - [Step 4: Parametrize Templates](#step-4-parametrize-templates)
- [Testing the Application](#testing-the-application)
- [Key Functionalities](#key-functionalities)
  - [Locale Selection](#locale-selection)
  - [Timezone Selection](#timezone-selection)
  - [Date and Time Localization](#date-and-time-localization)
- [Examples](#examples)
  - [User Locale and Timezone Settings](#user-locale-and-timezone-settings)
  - [Example Translations File](#example-translations-file)
  - [Example URL Queries](#example-url-queries)
- [Resources](#resources)

---

## Introduction

This project demonstrates implementing internationalization (i18n) in a Flask web application using Flask-Babel and pytz. i18n allows an application to adapt to different languages and timezones without modifying the core codebase, enhancing user experience for a global audience. Here, we support multiple languages, display locale-based messages, and show timezone-adjusted dates and times.

## Overview of i18n (Internationalization)

**i18n**, short for *internationalization*, is the process of designing and developing software so that it can be easily adapted to different languages, regions, and cultures without requiring engineering changes. The term "i18n" is derived from the word *internationalization* itself, with "18" representing the number of letters between the first "i" and the last "n".

### What is i18n?

i18n is a critical aspect of software development, especially for applications intended for a global audience. By implementing i18n, developers allow their applications to present language-specific and region-specific information to users. This encompasses:
1. **Language Localization**: Translating text, formatting dates and numbers, adjusting layout, and customizing other content based on a user’s preferred language.
2. **Time Zone Handling**: Adapting timestamps and time zone information to align with a user’s local time zone.
3. **Cultural Customization**: Modifying visuals, symbols, and certain functionalities (e.g., currency format or date format) to match cultural expectations.

### Why is i18n Important?

1. **Improved User Experience**: By showing content in a user's native language and preferred format, users have a more comfortable, relatable experience.
2. **Wider Audience Reach**: i18n enables applications to reach and engage with a global audience, enhancing inclusivity and accessibility.
3. **Compliance and Accessibility**: Many countries have legal requirements for accessibility and multi-language support in public-facing applications.

### How is i18n Implemented?

Internationalization is generally achieved through:
- **Message Translation**: Extracting translatable strings (words, phrases, etc.) from the code and translating them into multiple languages.
- **Locale Selection**: Allowing users or the system to specify their locale, a setting that informs the app which language and formatting preferences to use.
- **Date and Time Localization**: Formatting dates and times according to local conventions, such as showing dates in "DD/MM/YYYY" or "MM/DD/YYYY" format based on location.
- **Time Zone Adjustments**: Converting timestamps to reflect a user's specific time zone using libraries like `pytz` in Python.

### i18n in Web Development with Flask

In a Flask application, internationalization can be facilitated with the **Flask-Babel** extension, which provides essential i18n features, including:
- **Locale Selection**: Detecting and applying the preferred language.
- **Date and Time Formatting**: Formatting dates and times based on user locale.
- **Message Translation**: Allowing message strings to be translated and displayed in the user’s language.

For time zones, **pytz** is used to handle conversion between time zones, ensuring that times are accurate for each user's location. Flask-Babel integrates seamlessly with Flask and, combined with `pytz`, provides a robust foundation for creating multilingual and timezone-aware applications.

## Requirements

- **Python** 3.7+
- **Flask** - A lightweight WSGI web application framework.
- **Flask-Babel** - An extension to add i18n to Flask apps.
- **pytz** - A library to handle timezones in Python.

Install dependencies with:

```bash
pip3 install flask flask_babel pytz
```

## Key Concepts

### Flask-Babel
`Flask-Babel` is an extension for Flask applications to support localization by providing:
- Locale-aware date/time formatting
- Message translation
- Language selection through request parameters, user preferences, or browser headers

### pytz
`pytz` is a Python library that enables timezone conversion and localization based on standard time zones. It’s commonly used for displaying dates and times in users’ local time zones.

### i18n (Internationalization)
i18n is the process of designing an application for different languages and locales. Here, we support English and French, and allow users to select their preferred language through URL parameters, user settings, or request headers.

---

## Project Structure

The project structure includes core application files, templates, configuration files, and translation directories for supported languages.

```
.
├── 0x02-i18n
│   ├── app.py                     # Main Flask application file
│   ├── templates
│   │   └── index.html             # Template with translatable strings
│   ├── babel.cfg                  # Babel config file for extracting translations
│   ├── translations               # Folder containing language translations
│   │   ├── en
│   │   │   └── LC_MESSAGES
│   │   │       ├── messages.po    # English translations
│   │   │       └── messages.mo    # Compiled translation file
│   │   └── fr
│       └── LC_MESSAGES
│           ├── messages.po        # French translations
│           └── messages.mo        # Compiled translation file
```

---

## Setup Instructions

### Step 1: Install Dependencies

Install `Flask`, `Flask-Babel`, and `pytz`:

```bash
pip3 install flask flask_babel pytz
```

### Step 2: Create the Flask Application

Create the main application file `app.py`, with routes, locale, and timezone handling.

#### Example `app.py`:

```python
#!/usr/bin/env python3
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext
from pytz import timezone, UnknownTimeZoneError
import pytz

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'
app.config['LANGUAGES'] = ['en', 'fr']

# Initialize Babel
babel = Babel(app)

# Mock users with preferred locale and timezone
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

# Set locale from URL, user settings, or request headers
@babel.localeselector
def get_locale():
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    user = g.get('user')
    if user and user['locale'] in app.config['LANGUAGES']:
        return user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])

# Set timezone from URL, user settings, or default
@babel.timezoneselector
def get_timezone():
    tzname = request.args.get('timezone')
    if tzname:
        try:
            return timezone(tzname)
        except UnknownTimeZoneError:
            pass
    user = g.get('user')
    if user:
        try:
            return timezone(user['timezone'])
        except UnknownTimeZoneError:
            pass
    return timezone(app.config['BABEL_DEFAULT_TIMEZONE'])

@app.before_request
def before_request():
    user_id = request.args.get('login_as')
    if user_id:
        g.user = users.get(int(user_id))
    else:
        g.user = None

@app.route('/')
def index():
    current_time = babel.format_datetime()
    return render_template('index.html', current_time=current_time)

if __name__ == '__main__':
    app.run(debug=True)
```

### Step 3: Set Up Translations

1. Create a Babel configuration file `babel.cfg`:

   ```plaintext
   [python: **.py]
   [jinja2: **/templates/**.html]
   extensions=jinja2.ext.autoescape,jinja2.ext.with_ // or  jinja2.ext.do with jinja2 3.x.x and above
   ```

2. Extract messages for translation:

   ```bash
   pybabel extract -F babel.cfg -o messages.pot .
   ```

3. Initialize translations for English and French:

   ```bash
   pybabel init -i messages.pot -d translations -l en
   pybabel init -i messages.pot -d translations -l fr
   ```

4. Edit `translations/en/LC_MESSAGES/messages.po` and `translations/fr/LC_MESSAGES/messages.po` to add translations.

5. Compile translations:

   ```bash
   pybabel compile -d translations
   ```

### Step 4: Parametrize Templates

In your template (`index.html`), use the `_()` or `gettext()` functions to mark translatable strings.

#### Example `index.html`:

```html
<!DOCTYPE html>
<html lang="{{ g.get('locale', 'en') }}">
<head>
    <meta charset="UTF-8">
    <title>{{ _('Welcome to the Application') }}</title>
</head>
<body>
    <h1>{{ _('Hello world!') }}</h1>
    <p>
        {% if g.user %}
            {{ _('You are logged in as %(username)s.', username=g.user['name']) }}
        {% else %}
            {{ _('You are not logged in.') }}
        {% endif %}
    </p>
    <p>{{ _('The current time is %(current_time)s.', current_time=current_time) }}</p>
</body>
</html>
```

---

## Testing the Application

1. **Default Language**: Go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to see the app in the default language (English).
2. **Switch Language**: Use `?locale=fr` to view the app in French, or `?locale=en` for English.
3. **User Login Simulation**: Add `?login_as=1` or other IDs to simulate user preferences.

---

## Key Functionalities

### Locale Selection
The app selects the language in this order:
1. URL parameter (`?locale=fr`)
2. User settings (if logged in)
3. Browser language preferences

### Timezone Selection
The timezone is selected in this order:
1. URL parameter (`?timezone=Europe/Paris`)
2. User settings (if logged in)
3. Default timezone (UTC)

### Date and Time Localization
Using `babel.format_datetime()`, timestamps are displayed in the user’s timezone.

---

## Examples

### User Locale and Timezone Settings

```python
# Example user dictionary
users = {
    1: {"name": "Balou", "locale": "fr", "

timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
}
```

### Example Translations File

Inside `translations/fr/LC_MESSAGES/messages.po`:

```plaintext
msgid "Welcome to the Application"
msgstr "Bienvenue dans l'application"
```

### Example URL Queries

- `http://127.0.0.1:5000/?locale=fr&timezone=Europe/Paris`
- `http://127.0.0.1:5000/?login_as=2`

## Resources
- [Flask i18n tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xiii-i18n-and-l10n)
- [Flask-Babel Documentation](https://pythonhosted.org/Flask-Babel/)
- [pytz Documentation](https://pythonhosted.org/pytz/)

--- 

This README provides an extensive guide to set up, run, and test multi-language and timezone-aware features in a Flask app using i18n.
