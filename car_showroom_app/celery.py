import os

from core.celery_tasks import tasks

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "car_showroom_app.settings")

app = Celery("car_showroom_app")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    "celery_task": {
        "task": "core.celery_tasks.tasks.sample_task",
        "schedule": crontab(minute="*/10"),
    },
    # "buy_car": {
    #     "task": "core.celery_tasks.tasks.showroom_buy_cars",
    #     "schedule": crontab(minute="*/1"),
    # },
}
