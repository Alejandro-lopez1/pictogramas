from .base import *

DEBUG = True

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
]

INSTALLED_APPS += [
    "rest_framework",
    "corsheaders",

    "apps.pictograms",
    "apps.projects",
    "apps.templates_app",
    "apps.exports",
]
