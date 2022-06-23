"""Models for Customer"""

from core.abstractmodels.common_info import Information
from core.abstractmodels.date_fields import DateAddedUpdated
from core.filters_models.decimal_range_field import DecimalRangeField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Customer(DateAddedUpdated, Information):
    age = models.IntegerField(
        validators=[MinValueValidator(14), MaxValueValidator(150)]
    )
    sex = models.CharField(max_length=6)
    driver_licence = models.BooleanField(default=True)

    class Meta:
        db_table = "customer"

    def __str__(self):
        template = "{0.name} {0.age} {0.sex} {0.country} {0.email}"
        return template.format(self)


class CustomerOrder(DateAddedUpdated):
    customer = models.ForeignKey(
        Customer, on_delete=models.PROTECT, related_name="customer_orders", null=True
    )
    desired_car = models.JSONField(
        encoder=None,
        decoder=None,
        default={
            "make": "audi",
            "model": "q7",
            "color": "red",
            "year": "2010",
            "engine": 3.0,
            "body_type": "sedan",
        },
    )
    price = DecimalRangeField(max_digits=20, decimal_places=2, min_value=0.00)

    class Meta:
        db_table = "customer_order"

    def __str__(self):
        template = "{0.customer} {0.desired_car} {0.price} {0.is_active}"
        return template.format(self)
