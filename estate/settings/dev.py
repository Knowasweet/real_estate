from .base import *

EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_PORT = env('EMAIL_PORT')
DEFAULT_FROM_EMAIL = 'info@estate.com'
DOMAIN = env('DOMAIN')
SITE_NAME = 'Estate'

DATABASES = {
    'default': {
        'ENGINE': env('PG_ENGINE'),
        'NAME': env('PG_NAME'),
        'USER': env('PG_USER'),
        'PASSWORD': env('PG_PASSWORD'),
        'HOST': env('PG_HOST'),
        'PORT': env('PG_PORT'),
    }
}

CELERY_BROKER_URL = env('CELERY_BROKER')
CELERY_RESULT_BACKEND = env('CELERY_BACKEND')
