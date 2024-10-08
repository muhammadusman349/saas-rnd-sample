import os
from celery import Celery
# from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cfehome.settings")

app = Celery("cfehome")

# Update your Celery config here
# app.conf.update(
#     broker_connection_retry_on_startup=True,
# )
# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

# command for celery server
# celery -A cfehome worker --pool=solo -l info