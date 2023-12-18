"""
Django settings for project_name project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

from django.utils.log import DEFAULT_LOGGING

import dj_database_url
from decouple import Csv, config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", default=False, cast=bool)

ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="127.0.0.1,localhost", cast=Csv())

if DEBUG:
    INTERNAL_IPS = [
        "127.0.0.1",
    ]
    
# Application definition

INSTALLED_APPS = [
    "django_extensions",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Third-party
    "debug_toolbar",
]

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "project_name.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "project_name.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": dj_database_url.config(
        default=config("DATABASE_URL", default="sqlite:///db.sqlite3"),
        conn_max_age=600,
    )
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# https://docs.djangoproject.com/en/4.2/howto/static-files/deployment/
STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_DIRS = [
    BASE_DIR / "assets",
]


STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = "/upload/"

MEDIA_ROOT = BASE_DIR / "upload"

# ==============================================================================
# LOGGING SETTINGS
# ==============================================================================

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": DEFAULT_LOGGING["filters"],
    "formatters": DEFAULT_LOGGING["formatters"],
    "handlers": {
        **DEFAULT_LOGGING["handlers"],
        "rotating_file": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "log.log",
            "backupCount": 10,
            "maxBytes": 1e7,  # 10 Mega Bytes
        },
    },
    "loggers": {
        **DEFAULT_LOGGING["handlers"],
        "django": {
            "handlers": ["console", "rotating_file", "mail_admins"],
            "level": "INFO",
        },
        "django.server": {
            "handlers": ["django.server", "rotating_file"],
            "level": "INFO",
            "propagate": False,
        },
    },
}


##############################################
#             PRODUCTION SETTINGS            #
##############################################

if not DEBUG:
    # ==============================================================================
    # EMAIL SETTINGS
    # ==============================================================================

    EMAIL_HOST = "smtp.google.com"

    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

    SERVER_EMAIL = config("SERVER_EMAIL")

    EMAIL_USE_TLS = True

    EMAIL_HOST_USER = config("EMAIL_HOST_USER")

    EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")

    EMAIL_PORT = config("EMAIL_PORT", default=25, cast=int)

    # ==============================================================================
    # SECURITY SETTINGS
    # ==============================================================================

    CSRF_COOKIE_SECURE = False

    CSRF_COOKIE_HTTPONLY = False

    SECURE_HSTS_SECONDS = 60 * 60 * 24 * 7 * 52  # one year

    SECURE_HSTS_INCLUDE_SUBDOMAINS = False

    SECURE_SSL_REDIRECT = False

    SECURE_BROWSER_XSS_FILTER = False

    SECURE_CONTENT_TYPE_NOSNIFF = False

    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

    SESSION_COOKIE_SECURE = False
