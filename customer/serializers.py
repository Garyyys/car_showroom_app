from dealer.serializers import CarSerializer
from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers

from customer.models import Customer, CustomerOrder


class CustomerOrderSerializer(serializers.ModelSerializer):
    car = CarSerializer(read_only=True)

    class Meta:
        model = CustomerOrder
        fields = ["is_available", "price", "car"]


class CustomerSerializer(CountryFieldMixin, serializers.ModelSerializer):
    customer_orders = CustomerOrderSerializer(read_only=True, many=True)

    # TODO: check is available status for orders
    class Meta:
        model = Customer
        fields = [
            "name",
            "email",
            "balance",
            "country",
            "age",
            "sex",
            "driver_licence",
            "customer_orders",
        ]


class CustomerShortInfoSerializer(CountryFieldMixin, serializers.ModelSerializer):
    number_of_purchases = serializers.IntegerField()

    class Meta:
        model = Customer
        fields = ["name", "number_of_purchases"]
