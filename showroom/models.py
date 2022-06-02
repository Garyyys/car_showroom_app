from django.db import models

from core.abstractmodels.common_info import Information
from core.abstractmodels.date_fields import DateAdded, DateAddedUpdated
from core.abstractmodels.discount import Discount

# from core.filters_models.decimal_range_field import DecimalRangeField


class Showroom(DateAddedUpdated, Information):
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
    # cars = models.ManyToManyField('dealer.Car', through='ShowroomCarForSale')
    def __str__(self):
        template = "{0.name} {0.country} {0.email} {0.is_available}"
        return template.format(self)


# class ShowroomCarForSale(models.Model):
#     showroom = models.ForeignKey(Showroom, on_delete=models.CASCADE)
#     car = models.ForeignKey('dealer.Car', on_delete=models.CASCADE)
#     # TODO: delete this field
#     total_car = models.PositiveIntegerField()
#     price = DecimalRangeField(max_digits=20, decimal_places=2, min_value=0.00)
#
#     def __str__(self):
#         template = '{0.showroom} {0.car} {0.total_car} {0.price}'
#         return template.format(self)


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
