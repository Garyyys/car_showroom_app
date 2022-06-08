from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Discount(models.Model):
    name = models.CharField(max_length=100, default="test2")
    description = models.TextField(null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    amount_of_discount = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

    class Meta:
        abstract = True
