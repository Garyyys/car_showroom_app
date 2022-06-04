from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers

from dealer.serializers import CarSerializer

from .models import *


class CustomerOrderSerializer(serializers.ModelSerializer):
    car = CarSerializer(read_only=True)

    class Meta:
        model = CustomerOrder
        fields = ["is_available", "price", "car", "customer"]


class CustomerSerializer(CountryFieldMixin, serializers.ModelSerializer):
    customer_orders = CustomerOrderSerializer(read_only=True, many=True)

    class Meta:
        model = Customer
        fields = ["name", "email", "balance", "country", "age", "sex", "driver_licence", "customer_orders"]
