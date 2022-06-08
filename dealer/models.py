from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from core.abstractmodels.common_info import Information
from core.abstractmodels.date_fields import DateAddedUpdated, DateUpdatedAdded
from core.abstractmodels.discount import Discount
from core.filters_models.decimal_range_field import DecimalRangeField


class Dealer(DateAddedUpdated, Information):
    found_year = models.DateField()
    description = models.TextField(null=True)
    number_of_buyers = models.PositiveIntegerField(default=0)

    def __str__(self):
        template = "{0.name} {0.country} {0.email}" "{0.number_of_buyers} {0.is_available}"
        return template.format(self)


class Car(DateUpdatedAdded):
    CHOICES = (
        ("SEDAN", "Седан"),
        ("COUPE", "Купе"),
        ("SPORTS CAR", "Спорт кар"),
        ("STATION WAGON", "Универсал"),
        ("HATCHBACK", "Хэтчбэк"),
        ("CONVERTIBLE", "Кабриолет"),
        ("MINIVAN", "Минивэн"),
    )
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    year = models.IntegerField(validators=[MinValueValidator(1960), MaxValueValidator(3000)])
    engine = DecimalRangeField(max_digits=3, decimal_places=1, min_value=0.6, max_value=9.0)
    body_type = models.CharField(max_length=100, choices=CHOICES)
    price = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    showroom = models.ForeignKey(
        "showroom.Showroom", null=True, blank=True, on_delete=models.SET_NULL, related_name="showrooms_cars"
    )
    dealer = models.ForeignKey("Dealer", null=True, blank=True, on_delete=models.PROTECT, related_name="dealers_cars")
    customer = models.ForeignKey(
        "customer.Customer", null=True, blank=True, on_delete=models.SET_NULL, related_name="customers_cars"
    )

    def __str__(self):
        template = (
            "{0.make} {0.model} {0.color} {0.year} {0.engine}" "{0.body_type} {0.price}" " {0.showroom} {0.customer}"
        )
        return template.format(self)


class DiscountDealer(DateAddedUpdated, Discount):
    dealer = models.ForeignKey("Dealer", on_delete=models.PROTECT, related_name="dealer_discount", null=True)
    dealer_car = models.ForeignKey(Car, on_delete=models.PROTECT, related_name="dealer_car", null=True)

    def __str__(self):
        template = "{0.dealer} {0.start_time} {0.end_time} {0.dealer_car}" "{0.amount_of_discount} {0.is_available}"
        return template.format(self)
