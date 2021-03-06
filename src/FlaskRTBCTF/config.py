import os
from datetime import datetime
import pytz

from .helpers import handle_secret_key

# Flask related Configurations
# Note: DO NOT FORGET TO CHANGE 'SECRET_KEY' !


class Config:
    SECRET_KEY = handle_secret_key()
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "sqlite:///site.db"
    # For local use, one can simply use SQLlite with: 'sqlite:///site.db'
    # For deployment on Heroku use: `os.environ.get('DATABASE_URL')`
    # in all other cases: `os.environ.get('SQLALCHEMY_DATABASE_URI')`
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False  # Turn DEBUG OFF before deployment
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("EMAIL_USER")
    MAIL_PASSWORD = os.environ.get("EMAIL_PASS")


# CTF related Configuration
# Add some information about organization and specify CTF name

organization = {
    "ctfname": "RootTheBox CTF",
    "name": "Abs0lut3Pwn4g3",
    "website": {
        "url": "https://Abs0lut3Pwn4g3.github.io/",
        "name": "Official Abs0lut3Pwn4g3 Website",
    },
    "website_2": {"url": "https://twitter.com/abs0lut3pwn4g3", "name": "Twitter"},
    "website_3": {"url": "https://github.com/abs0lut3pwn4g3", "name": "GitHub"},
}

# Specify CTFs Running Time
# We do not recommend changing the Timezone.

RunningTime = {
    "from": datetime(2019, 7, 7, 15, 00, 00, 0, pytz.utc),
    "to": datetime(2023, 7, 8, 0, 00, 00, 0, pytz.utc),
    "TimeZone": "UTC",
}

# Logging: Set to 'True' to enable Logging in Admin Views.
# We recommend to leave it on. It is more than just errors ;)

LOGGING = True
