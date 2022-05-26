from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django_countries.fields import CountryField
from core.abstractmodels.date_fields import DateAddedUpdated, DateUpdatedAdded
from core.abstractmodels.common_info import Information
from core.abstractmodels.discount import Discount
from core.filters_models.decimal_range_field import DecimalRangeField


class Dealer(DateAddedUpdated, Information):
    found_year = models.DateField()
    description = models.TextField(null=True)
    number_of_buyers = models.PositiveIntegerField(default=0)
    cars = models.ManyToManyField('Car', through='DealerCarForSale')

    def __str__(self):
        template = '{0.name} {0.country} {0.email}' \
                   '{0.number_of_buyers} {0.is_available}'
        return template.format(self)


class Car(DateUpdatedAdded):
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    year = models.IntegerField(validators=[MinValueValidator(1960), MaxValueValidator(3000)])
    engine = DecimalRangeField(max_digits=3, decimal_places=1, min_value=0.6, max_value=9.0)
    body_type = models.CharField(max_length=20)

    def __str__(self):
        template = '{0.make} {0.model} {0.color} {0.year} {0.engine}' \
                   '{0.body_type}'
        return template.format(self)


class DealerCarForSale(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)
    price = DecimalRangeField(max_digits=20, decimal_places=2, min_value=3000)

    def __str__(self):
        template = '{0.supplier} {0.car} {0.price}'
        return template.format(self)


class DiscountDealer(DateAddedUpdated, Discount):
    id_supplier = models.ForeignKey('customer.Customer', on_delete=models.PROTECT, related_name="discount_id_dealer")
    id_car = models.ForeignKey(Car, on_delete=models.PROTECT, related_name="discount_dealer_id_car")

    def __str__(self):
        template = '{0.id_supplier} {0.start_time} {0.end_time} {0.id_car}' \
                   '{0.amount_of_discount} {0.is_available}'
        return template.format(self)