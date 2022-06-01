from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers
from dealer.serializers import CarSerializer
from .models import *


class ShowroomSerializer(CountryFieldMixin, serializers.ModelSerializer):
    class Meta:
        model = Showroom
        fields = '__all__'
        depth = 1

class ShowroomCarForSaleSerializer(serializers.ModelSerializer):
    cars = CarSerializer(read_only=True)
    showroom = ShowroomSerializer(read_only=True)

    class Meta:
        model = ShowroomCarForSale
        exclude = ['car']
        # fields = '__all__'


class DiscountShowroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountShowroom
        fields = '__all__'