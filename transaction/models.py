from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from core.abstractmodels.date_fields import DateAdded
from core.filters_models.decimal_range_field import DecimalRangeField


class SalesShowroomToCustomer(DateAdded, models.Model):
    id_showroom = models.ForeignKey('showroom.Showroom', on_delete=models.PROTECT,
                                    related_name="sales_buyers_id_showroom")
    id_buyer = models.ForeignKey('customer.Customer', on_delete=models.PROTECT, related_name="sales_id_buyers")
    id_car = models.ForeignKey('dealer.Car', on_delete=models.PROTECT, related_name="sales_buyer_id_car")
    price = DecimalRangeField(max_digits=20, decimal_places=2, min_value=0.00)
    amount_of_discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(30)])

    def __str__(self):
        template = '{0.id_showroom} {0.id_buyer} {0.id_car}' \
                   '{0.price} {0.amount_of_discount} {0.added_date}'
        return template.format(self)


class SalesDealerToShowroom(DateAdded, models.Model):
    id_showroom = models.ForeignKey('showroom.Showroom', on_delete=models.PROTECT, related_name="sales_id_showroom")
    id_supplier = models.ForeignKey('dealer.Dealer', on_delete=models.PROTECT, related_name="sales_id_dealer")
    id_car = models.ForeignKey('dealer.Dealer', on_delete=models.PROTECT, related_name="sales_showroom_id_car")
    price = DecimalRangeField(max_digits=20, decimal_places=2, min_value=0.00)
    amount_of_discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(30)])

    def __str__(self):
        template = '{0.id_showroom} {0.id_supplier} {0.id_car}' \
                   '{0.price} {0.amount_of_discount} {0.added_date}'
        return template.format(self)
