from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers

from .models import *


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ["make", "model", "body_type", "color", "year", "engine"]


class DealerCarForSaleSerializer(CountryFieldMixin, serializers.ModelSerializer):
    car = CarSerializer()

    class Meta:
        model = DealerCarForSale
        fields = ["car", "price"]


class DealerSerializer(CountryFieldMixin, serializers.ModelSerializer):
    dealers_cars = DealerCarForSaleSerializer(read_only=True, many=True)

    class Meta:
        model = Dealer
        fields = ["name", "email", "found_year", "description", "dealers_cars"]


class DiscountDealerSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountDealer
        fields = "__all__"
