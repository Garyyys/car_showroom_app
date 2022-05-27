from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django_countries.fields import CountryField
from core.abstractmodels.date_fields import DateAddedUpdated, DateAdded
from core.abstractmodels.discount import Discount
from core.abstractmodels.common_info import Information
from core.filters_models.decimal_range_field import DecimalRangeField


class Showroom(DateAddedUpdated, Information):
    specification = models.JSONField(encoder=None, decoder=None)
    cars = models.ManyToManyField('dealer.Car', through='ShowroomCarForSale')

    def __str__(self):
        template = '{0.name} {0.country} {0.email} {0.is_available}'
        return template.format(self)


class ShowroomCarForSale(models.Model):
    showroom = models.ForeignKey(Showroom, on_delete=models.CASCADE)
    car = models.ForeignKey('dealer.Car', on_delete=models.CASCADE)
    total_car = models.PositiveIntegerField()
    price = DecimalRangeField(max_digits=20, decimal_places=2, min_value=0.00)

    def __str__(self):
        template = '{0.showroom} {0.car} {0.cars_count} {0.price}'
        return template.format(self)


class DiscountShowroom(DateAddedUpdated, Discount):
    id_showroom = models.ForeignKey(Showroom, on_delete=models.PROTECT, related_name="discount_id_showroom")
    id_car = models.ForeignKey('dealer.Car', on_delete=models.PROTECT, related_name="discount_showrooms_id_car")

    def __str__(self):
        template = '{0.id_showroom} {0.start_time} {0.end_time} {0.id_car}' \
                   '{0.amount_of_discount} {0.is_available}'
        return template.format(self)
