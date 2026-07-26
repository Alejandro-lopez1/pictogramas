from .base import *  # noqa: F401, F403

DEBUG = False

ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="", cast=Csv())  # noqa: F405

CORS_ALLOW_ALL_ORIGINS = False

CORS_ALLOWED_ORIGINS = config(  # noqa: F405
    "CORS_ALLOWED_ORIGINS",
    default="",
    cast=Csv(),
)

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"
