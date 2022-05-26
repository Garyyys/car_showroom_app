from rest_framework import serializers
from showroom.models import Showroom


class ShowRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Showroom
        fields = ('name', 'balance', 'email')