from django.db import models
from django_countries.fields import CountryField


class ShowRoom(models.Model):
    name = models.CharField(max_length=50)
    location = CountryField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    car_type = models.ForeignKey('CarType', on_delete=models.CASCADE)
    dealers = models.ManyToManyField('dealer.Dealer')




class CarType(models.Model):
    name = models.CharField(max_length=20)


class SRPrice(models.Model):
    value = models.PositiveIntegerField()
    showroom = models.ForeignKey('ShowRoom', related_name='prices', on_delete=models.CASCADE)
    model = models.ForeignKey('dealer.CarModel', on_delete=models.CASCADE)



class SRDiscount(models.Model):
    name = models.CharField(max_length=50)
    value = models.PositiveIntegerField()
    date_start = models.DateField()
    date_end = models.DateField()
    price = models.OneToOneField('SRDiscount', on_delete=models.CASCADE)

