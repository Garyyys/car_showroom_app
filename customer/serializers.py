""""""

from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers

from customer.models import Customer, CustomerOrder


class CustomerOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerOrder
        fields = [
            "is_active",
            "price",
            "desired_car",
        ]


class CustomerSerializer(CountryFieldMixin, serializers.ModelSerializer):
    customer_orders = CustomerOrderSerializer(read_only=True, many=True)

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
