from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django_countries.fields import CountryField

from core.abstractmodels.common_info import Information
from core.abstractmodels.date_fields import DateAddedUpdated, DateUpdatedAdded
from core.filters_models.decimal_range_field import DecimalRangeField


class Customer(DateUpdatedAdded, Information):
    age = models.IntegerField(validators=[MinValueValidator(14), MaxValueValidator(150)])
    sex = models.CharField(max_length=6)
    driver_licence = models.BooleanField(default=True)

    def __str__(self):
        template = "{0.name} {0.age} {0.sex} {0.country} {0.email}"
        return template.format(self)


class CustomerOrder(DateAddedUpdated):
    id_customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name="order_id_customers", null=True)
    id_car = models.ForeignKey("dealer.Car", on_delete=models.PROTECT, related_name="order_id_car")
    price = DecimalRangeField(max_digits=20, decimal_places=2, min_value=0.00)

    def __str__(self):
        template = "{0.id_customer} {0.id_car} {0.price} {0.is_available}"
        return template.format(self)
