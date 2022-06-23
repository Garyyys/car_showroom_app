from decimal import Decimal
from celery import shared_task
from celery.utils.log import get_task_logger

from dealer.models import Car, DiscountDealer, LoyaltyProgram
from django.db import transaction
from django.db.models import Q
from showroom.models import Showroom
from transaction.models import SalesDealerToShowroom

logger = get_task_logger(__name__)


@shared_task
def showroom_buy_cars():
    for showroom in Showroom.objects.all():
        showroom_preference = showroom.specification

        car_dealer_search = (
            Q(make__startswith=showroom_preference.get("make"))
            & Q(model__icontains=showroom_preference.get("model"))
            & Q(color__icontains=showroom_preference.get("color"))
            & Q(year__exact=showroom_preference.get("year"))
            & Q(engine__exact=showroom_preference.get("engine"))
            & Q(body_type__icontains=showroom_preference.get("body_type"))
        )

        dealer_cars = Car.objects.filter(
            car_dealer_search, showroom__isnull=True, customer__isnull=True
        ).order_by("price")
        for dealer_car in dealer_cars:
            with transaction.atomic():
                discount_dealer, created = DiscountDealer.objects.get_or_create(
                    showroom=showroom, dealer=dealer_car.dealer
                )
                price = Decimal(dealer_car.price) * (
                    (100 - Decimal(discount_dealer.discount) / 100)
                )
                if showroom.balance - price > 0:
                    SalesDealerToShowroom.objects.create(
                        showroom=showroom,
                        dealer=dealer_car.dealer,
                        car=dealer_car,
                        price=price,
                        amount_of_discount=discount_dealer.discount,
                    )

                    dealer_car.showroom = showroom
                    dealer_car.dealer = None
                    dealer_car.price += 100
                    dealer_car.save(update_fields=["showroom", "dealer", "price"])
                    showroom.balance -= price
                    showroom.save(update_fields=["balance"])
                    discount_dealer.bought_cars += 1
                    discount_dealer.save(update_fields=["bought_cars"])
                    loyality_program = (
                        LoyaltyProgram.objects.filter(
                            dealer=dealer_car.dealer,
                            min_bought_cars__lte=discount_dealer.bought_cars,
                        )
                        .order_by("-min_bought_cars")
                        .first()
                    )
                    if (
                        loyality_program
                        and loyality_program.program != discount_dealer.discount
                    ):
                        discount_dealer.discount = loyality_program.program
                        discount_dealer.save(update_fields=["discount"])
