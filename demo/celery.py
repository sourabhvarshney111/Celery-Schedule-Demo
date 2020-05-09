from __future__ import absolute_import

import os
import django

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE','demo.settings')
django.setup()

app = Celery('demo')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
