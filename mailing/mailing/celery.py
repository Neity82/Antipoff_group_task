from __future__ import absolute_import
import os
from celery import Celery

from mailing_hb.tasks import send_messages

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mailing.settings")

app = Celery("mailing")
app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(10.0, send_messages(), name="add every 10")

