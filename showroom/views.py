from rest_framework import generics
from .models import Showroom
from .serializers import ShowRoomSerializer


class ShowRoomAPIView(generics.ListAPIView):
    queryset = Showroom.objects.all()
    serializer_class = ShowRoomSerializer
