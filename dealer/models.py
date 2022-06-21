from core.abstractmodels.common_info import Information
from core.abstractmodels.date_fields import DateAddedUpdated, DateUpdatedAdded
from core.abstractmodels.discount import Discount
from core.filters_models.decimal_range_field import DecimalRangeField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from dealer.utils import DiscountRanks


class Dealer(DateAddedUpdated, Information):
    found_year = models.DateField()
    description = models.TextField(null=True)
    number_of_buyers = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = "dealer"

    def __str__(self):
        template = "{0.name} {0.country} {0.email}" "{0.number_of_buyers} {0.is_active}"
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
    year = models.IntegerField(
        validators=[MinValueValidator(1960), MaxValueValidator(3000)]
    )
    engine = DecimalRangeField(
        max_digits=3, decimal_places=1, min_value=0.6, max_value=9.0
    )
    body_type = models.CharField(max_length=100, choices=CHOICES)
    price = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    showroom = models.ForeignKey(
        "showroom.Showroom",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="showrooms_cars",
    )
    dealer = models.ForeignKey(
        "Dealer",
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name="dealers_cars",
    )
    customer = models.ForeignKey(
        "customer.Customer",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="customers_cars",
    )

    class Meta:
        db_table = "car"

    def __str__(self):
        template = (
            "{0.make} {0.model} {0.color} {0.year} {0.engine}"
            "{0.body_type} {0.price}"
            " {0.showroom} {0.customer}"
        )
        return template.format(self)



class DiscountDealer(models.Model):
    """
    Discounts Dealer - ShowRoom
    """

    discount = models.IntegerField(
        choices=DiscountRanks.DISCOUNT_CHOICES, default=DiscountRanks.REGULAR
    )
    bought_cars = models.PositiveIntegerField(default=0)
    showroom = models.ForeignKey(
        "showroom.Showroom",
        related_name="showroom_discounts",
        on_delete=models.CASCADE,
        null=True,
    )
    dealer = models.ForeignKey(
        "dealer.Dealer",
        related_name="dealer_discounts",
        on_delete=models.CASCADE,
        null=True,
    )

    class Meta:
        db_table = "dealer_discount"
        unique_together = ["showroom", "dealer"]

    def __str__(self):
        template = "{0.discount} {0.bought_cars} {0.showroom}" "{0.dealer}"
        return template.format(self)


class LoyaltyProgram(models.Model):
    """
    Loyalty program is unique for every dealer
    and discount by number of bought cars
    is different.

    min_bought_cars: minimum value for achieve this particular program.

    DealerDiscount.discount updates depends on LoyaltyProgram
    """

    dealer = models.ForeignKey(
        "dealer.Dealer", related_name="dealer_loyalties", on_delete=models.CASCADE
    )
    program = models.IntegerField(
        choices=DiscountRanks.DISCOUNT_CHOICES, default=DiscountRanks.REGULAR
    )
    min_bought_cars = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ["dealer", "program"]

    def __str__(self):
        if self.dealer:
            return f"{self.dealer} - {self.program}"
        return "New Loyalty Program"
