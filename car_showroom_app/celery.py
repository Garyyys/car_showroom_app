import os


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
    "showroom_buy_car": {
        "task": "dealer.tasks.showroom_buy_cars",
        "schedule": crontab(minute="*/1"),
    },
    "customer_buy_car": {
        "task": "showroom.tasks.customer_buy_car",
        "schedule": crontab(minute="*/1"),
    },
}
