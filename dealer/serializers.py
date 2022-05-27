from rest_framework import serializers
from django_countries.serializers import CountryFieldMixin
from .models import *


class DealerSerializer(CountryFieldMixin, serializers.ModelSerializer):
    class Meta:
        model = Dealer
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class DealerCarForSaleSerializer(CountryFieldMixin, serializers.ModelSerializer):
    car = CarSerializer(read_only=True)
    supplier = DealerSerializer(read_only=True)

    class Meta:
        model = DealerCarForSale
        fields = '__all__'


class DiscountDealerSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountDealer
        fields = '__all__'
