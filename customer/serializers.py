from rest_framework import serializers
from django_countries.serializers import CountryFieldMixin
from dealer.serializers import CarSerializer
from .models import *


class CustomerSerializer(CountryFieldMixin, serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class CustomerOrderSerializer(serializers.ModelSerializer):
    id_car = CarSerializer(read_only=True)
    id_buyer = CustomerSerializer(read_only=True)

    class Meta:
        model = CustomerOrder
        fields = '__all__'

