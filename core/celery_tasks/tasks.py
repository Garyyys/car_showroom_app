from celery import shared_task
from celery.utils.log import get_task_logger

from dealer.models import Car, DiscountDealer, LoyaltyProgram

from django.db import transaction

from django.db.models import Q


logger = get_task_logger(__name__)


@shared_task
def sample_task():
    logger.info("The sample task just ran.")
