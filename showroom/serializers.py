from customer.models import Customer
from customer.serializers import CustomerShortInfoSerializer
from dealer.models import Car
from django.db.models import Count, F
from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers

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
    buyers = serializers.SerializerMethodField()

    class Meta:
        model = Showroom
        fields = ["name", "country", "email", "balance", "cars", "total_cars", "buyers"]

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

    def get_buyers(self, instance):
        queryset = Showroom.objects.get(pk=instance.id)
        buyers = (
            queryset.showroom.all()
            .values(name=F("customer__name"))
            .annotate(number_of_purchases=Count("customer"))
            .order_by()
        )
        serializer_data = CustomerShortInfoSerializer(buyers, many=True).data

        return serializer_data


class ShortShowroomSerializer(CountryFieldMixin, serializers.ModelSerializer):
    class Meta:
        model = Showroom
        fields = ["name", "country"]


class DiscountShowroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountShowroom
        fields = "__all__"
