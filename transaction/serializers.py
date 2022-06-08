from customer.serializers import CustomerShortInfoSerializer
from dealer.serializers import CarSerializer
from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers
from showroom.serializers import ShortShowroomSerializer

from transaction.models import SalesDealerToShowroom, SalesShowroomToCustomer


class SalesShowroomToBuyersSerializer(CountryFieldMixin, serializers.ModelSerializer):
    showroom = ShortShowroomSerializer(read_only=True)
    customer = CustomerShortInfoSerializer(read_only=True)
    car = CarSerializer(read_only=True)

    class Meta:
        model = SalesShowroomToCustomer
        fields = ["showroom", "customer", "car", "price", "amount_of_discount"]


class SalesDealerToShowroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesDealerToShowroom
        fields = "__all__"
