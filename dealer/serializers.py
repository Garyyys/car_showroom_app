from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers

from .models import *


class CarSerializer(serializers.ModelSerializer):
    total_models = serializers.IntegerField()

    class Meta:
        model = Car
        fields = ["make", "model", "body_type", "color", "year", "engine", "total_models"]


# class DealerCarForSaleSerializer(CountryFieldMixin, serializers.ModelSerializer):
#     car = CarSerializer()
#
#     class Meta:
#         model = DealerCarForSale
#         fields = ["car", "price"]


class DealerSerializer(CountryFieldMixin, serializers.ModelSerializer):
    # dealers_cars = DealerCarForSaleSerializer(read_only=True, many=True)
    dealer_cars = serializers.SerializerMethodField()
    cars_list = serializers.SerializerMethodField()

    class Meta:
        model = Dealer
        fields = ["name", "email", "found_year", "description"]

    # get_cars


class DiscountDealerSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountDealer
        fields = "__all__"
