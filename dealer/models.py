from django.db import models
from django_countries.fields import CountryField


class Dealer(models.Model):
    name = models.CharField(max_length=50)
    found_year = models.DateField()
    address = CountryField()
    # число шоурумов
    count_sr = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)


class Make(models.Model):
    name = models.CharField(max_length=100)
    dealer = models.OneToOneField('Dealer', on_delete=models.CASCADE)


class CarModel(models.Model):
    name = models.CharField(max_length=50)
    found_year = models.DateField()
    make = models.ForeignKey('Make', related_name='models', on_delete=models.CASCADE)


class DPrice(models.Model):
    value = models.PositiveIntegerField()
    model = models.OneToOneField('CarModel', on_delete=models.CASCADE)


class DDiscount(models.Model):
    name = models.CharField(max_length=50)
    value = models.PositiveIntegerField()
    date_start = models.DateField()
    date_end = models.DateField()
    price = models.OneToOneField('DPrice', on_delete=models.CASCADE)

