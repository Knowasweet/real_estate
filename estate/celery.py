from __future__ import absolute_import
import os
from celery import Celery
from estate.settings import base

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'estate.settings.dev')

app = Celery('estate')

app.config_from_object('estate.settings.dev', namespace='CELERY')

app.autodiscover_tasks(lambda: base.INSTALLED_APPS)
