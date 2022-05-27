from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Discount(models.Model):
    description = models.TextField(null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    amount_of_discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])

    class Meta:
        abstract = True