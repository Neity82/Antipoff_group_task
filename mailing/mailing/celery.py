from __future__ import absolute_import
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mailing.settings")

app = Celery("mailing")
app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()


app.conf.beat_schedule = {
    'send-report-every-day': {
        'task': 'mailing_hb.tasks.send_messages',
        'schedule': crontab(hour=10, minute=30),
    },
}