from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers

from dealer.serializers import CarSerializer

from .models import *


class CustomerOrderSerializer(serializers.ModelSerializer):
    id_car = CarSerializer(read_only=True)

    class Meta:
        model = CustomerOrder
        fields = "__all__"
        depth = 1


class CustomerSerializer(CountryFieldMixin, serializers.ModelSerializer):
    order_id_customers = CustomerOrderSerializer(read_only=True, many=True)

    class Meta:
        model = Customer
        fields = ["name", "email", "balance", "country", "age", "sex", "driver_licence" "order_id_customers"]
