from django.db.models import Count
from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers

from dealer.models import Car
from dealer.serializers import CarSerializer

from .models import DiscountShowroom, Showroom

# class ShowroomCarForSaleSerializer(serializers.ModelSerializer):
#     car = CarSerializer(read_only=True)
#     total_models = serializers.IntegerField()
#
#     class Meta:
#         model = ShowroomCarForSale
#         fields = ['car', 'price', "total_models"]


class ShowroomSerializer(CountryFieldMixin, serializers.ModelSerializer):
    cars = serializers.SerializerMethodField()
    total_cars = serializers.SerializerMethodField()

    class Meta:
        model = Showroom
        fields = "__all__"

    def get_cars(self, instance):
        cars = Car.objects.filter(showroom=instance).values("model").annotate(total_models=Count("model")).order_by()
        serializer = CarSerializer(cars, many=True).data
        return serializer

    def get_total_cars(self, instance):
        return instance.car_set.all().count()


class DiscountShowroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountShowroom
        fields = "__all__"
