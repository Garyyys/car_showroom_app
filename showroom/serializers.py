from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from showroom.models import Showroom
from django.db.models import DecimalField

class ShowroomModel:
    def __init__(self, name, balance, email):
        self.name = name
        self.balance = balance
        self.email = email



class ShowRoomSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    balance = DecimalField()
    email = serializers.CharField(max_length=100)


def encode():
    model = ShowroomModel('AtlantM', 18.00, 'asdad@gmail.com')
    model_sr = ShowRoomSerializer(model)
    print(model_sr.data, type(model_sr), sep='\n')
    json = JSONRenderer().render(model_sr.data)
    print(model_sr.data, type(model_sr.data), sep='\n')
