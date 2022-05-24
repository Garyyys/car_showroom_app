from django.db import models


class SRTransaction(models.Model):
    showroom = models.ForeignKey('showroom.ShowRoom', on_delete=models.CASCADE)
    customer = models.OneToOneField('customer.Customer', on_delete=models.CASCADE)
    model = models.ForeignKey('dealer.CarModel', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    # количество проданных авто Клиент - Шоурум
    value = models.PositiveIntegerField()


class DTransaction(models.Model):
    showroom = models.ForeignKey('showroom.ShowRoom', on_delete=models.CASCADE)
    model = models.OneToOneField('dealer.CarModel', on_delete=models.CASCADE)
    dealer = models.ForeignKey('dealer.Dealer', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    # количество проданных авто Диллер - Шоурум
    value = models.PositiveIntegerField()


