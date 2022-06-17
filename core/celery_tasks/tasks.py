from celery import shared_task
from celery.utils.log import get_task_logger

# from dealer.models import Dealer
# from django.db.models import F, Q
# from showroom.models import Showroom

logger = get_task_logger(__name__)


@shared_task
def sample_task():
    logger.info("The sample task just ran.")


# @shared_task
# def showroom_buy_cars():
#     for showroom in Showroom.objects.all():
#         showroom_preference = showroom.specification
#
#         car_dealer_search = (
#             Q(car__make__startswith=showroom_preference.get("make"))
#             & Q(car__model__icontains=showroom_preference.get("model"))
#             & Q(car__color__icontains=showroom_preference.get("color"))
#             & Q(car__year__icontains=showroom_preference.get("year"))
#             & Q(car__engine__exact=showroom_preference.get("engine"))
#             & Q(car__body_type__=showroom_preference.get("body_type"))
#         )
#
#         #
#         dealer_cars = Dealer.objects.filter(car_dealer_search)
#         # .order_by(
#         #             # TODO: rewrite ordering field
#         #             # "-supplier__sale__percent"
#         #         )
#         #         showroom_cars = ShowroomSellCar.objects.filter(
#         #             showroom__name__iexact=showroom.name
#         #         )
#         #
#         for dealer_car in dealer_cars:
#
#             price = dealer_car.price
#
#             if SupplierSale.objects.filter(cars__pk=dealer_car.car.id).exists():
#                 sale = SupplierSale.objects.get(cars__pk=dealer_car.car.id)
#                 price -= price * sale.percent / 100
#
#             if price > showroom.balance:
#                 continue
#
#             showroom.balance -= price
#
#             showroom_cars.update_or_create(
#                 car=dealer_car.car,
#                 showroom=showroom,
#                 supplier=dealer_car.supplier,
#                 defaults={"count": F("count") + 1},
#             )
#
#             showroom.save()
