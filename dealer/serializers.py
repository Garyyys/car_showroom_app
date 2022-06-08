from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers

from .models import Car, Dealer, DiscountDealer


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ["make", "model", "body_type", "color", "year", "engine"]


class DealerSerializer(CountryFieldMixin, serializers.ModelSerializer):
    dealers_cars = CarSerializer(many=True, read_only=True)
    total_cars = serializers.SerializerMethodField()

    class Meta:
        model = Dealer
        fields = ["name", "email", "found_year", "description", "total_cars", "dealers_cars"]

    def get_total_cars(self, instance):
        return instance.dealers_cars.count()


class DiscountDealerSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountDealer
        fields = "__all__"
