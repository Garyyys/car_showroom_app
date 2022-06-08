from django.db.models import Count
from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers

from dealer.models import Car
from showroom.models import DiscountShowroom, Showroom


class ShowroomsCarsSerializer(serializers.ModelSerializer):
    # TODO: add uniquebuyers field
    # TODO: add separate serializer for count value of transactions for buyers
    total_models = serializers.IntegerField()

    class Meta:
        model = Car
        fields = [
            "make",
            "model",
            "total_models",
        ]


class MainShowroomSerializer(CountryFieldMixin, serializers.ModelSerializer):
    cars = serializers.SerializerMethodField()
    total_cars = serializers.SerializerMethodField()

    class Meta:
        model = Showroom
        fields = ["name", "country", "email", "balance", "cars", "total_cars"]

    def get_cars(self, instance):
        cars = (
            Car.objects.filter(showroom=instance)
            .values("model", "make")
            .annotate(total_models=Count("model"))
            .order_by()
        )
        serializer = ShowroomsCarsSerializer(cars, many=True).data
        return serializer

    def get_total_cars(self, instance):
        return instance.showrooms_cars.all().count()


class ShortShowroomSerializer(CountryFieldMixin, serializers.ModelSerializer):
    class Meta:
        model = Showroom
        fields = ["name", "country"]


class DiscountShowroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountShowroom
        fields = "__all__"
