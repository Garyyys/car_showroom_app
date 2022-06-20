from decimal import Decimal

from celery import shared_task
from celery.utils.log import get_task_logger

from customer.models import CustomerOrder
from dealer.models import Car
from django.db import transaction
from django.db.models import Q

from showroom.models import DiscountShowroom
from transaction.models import SalesShowroomToCustomer

logger = get_task_logger(__name__)


@shared_task
def customer_buy_car():
    for order in CustomerOrder.objects.all():
        if order.is_active:
            desired_car = order.desired_car
            desired_car_search = (
                Q(make__startswith=desired_car.get("make"))
                & Q(model__icontains=desired_car.get("model"))
                & Q(color__icontains=desired_car.get("color"))
                & Q(year__exact=desired_car.get("year"))
                & Q(engine__exact=desired_car.get("engine"))
                & Q(body_type__icontains=desired_car.get("body_type"))
            )
            showroom_cars = Car.objects.filter(
                desired_car_search, dealer__isnull=True, customer__isnull=True
            ).order_by("price")
            for showroom_car in showroom_cars:
                with transaction.atomic():
                    customer = order.customer
                    showroom = showroom_car.showroom
                    if customer.balance > 0:
                        discount = DiscountShowroom.objects.filter(
                            showrooms_discount=showroom,
                            discount_showroom_for_car=showroom_car,
                        ).first()
                        price = showroom_car.price * Decimal(
                            ((100 - discount.amount_of_discount) / 100)
                        )
                        SalesShowroomToCustomer.objects.create(
                            showroom=showroom,
                            customer=customer,
                            car=showroom_car,
                            price=price,
                            amount_of_discount=discount.amount_of_discount,
                        )
                        showroom.balance += price
                        showroom.save(update_fields=["balance"])
                        showroom_car.showroom = None
                        showroom_car.customer = order.customer
                        showroom_car.save(
                            update_fields=[
                                "showroom",
                                "customer",
                            ]
                        )
                        customer.balance -= price
                        customer.save(update_fields=["balance"])
                        order.is_active = False
                        order.save(update_fields=["is_active"])
