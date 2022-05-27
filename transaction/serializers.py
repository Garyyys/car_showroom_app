from rest_framework import serializers
from .models import *


class SalesShowroomToBuyersSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesShowroomToCustomer
        fields = '__all__'


class SalesDealerToShowroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesDealerToShowroom
        fields = '__all__'
