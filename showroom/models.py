from django.db import models

from core.abstractmodels.common_info import Information
from core.abstractmodels.date_fields import DateAdded, DateAddedUpdated
from core.abstractmodels.discount import Discount


class Showroom(DateAddedUpdated, Information):
    # TODO: add uniqbuyers field
    specification = models.JSONField(
        encoder=None,
        decoder=None,
        default={
            "make": "audi",
            "model": "q7",
            "color": "red",
            "year": "2010",
            "engine": 7.0,
            "body_type": "sedan",
        },
    )

    def __str__(self):
        template = "{0.name} {0.country} {0.email} {0.is_available}"
        return template.format(self)


class DiscountShowroom(DateAddedUpdated, Discount):
    showrooms_discount = models.ForeignKey(
        Showroom, on_delete=models.PROTECT, related_name="showrooms_discount", null=True
    )
    discount_showroom_for_car = models.ForeignKey(
        "dealer.Car", on_delete=models.PROTECT, related_name="discount_showroom_for_car", null=True
    )

    def __str__(self):
        template = "{0.id_showroom} {0.start_time} {0.end_time} {0.id_car}" "{0.amount_of_discount} {0.is_available}"
        return template.format(self)
