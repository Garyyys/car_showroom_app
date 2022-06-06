from django.db.models import Count
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from core.common_api_interface.common_api_interface import CustomViewSet

from .models import Showroom
from .serializers import ShowroomSerializer


class ShowroomsViewSet(CustomViewSet):
    queryset = Showroom.objects.all()
    serializer_class = ShowroomSerializer()

    # filterset_class = ShowroomFilter

    @action(methods=["get"], detail=False, url_path="list")
    def list_of_showrooms(self, request):
        showrooms = Showroom.objects.all()
        data = ShowroomSerializer(showrooms, many=True).data
        return Response({"Showrooms": data})

    @action(methods=["get"], detail=True, url_path="details")
    def detail_of_showroom(self, request, pk):
        dealer_detail = Showroom.objects.get(pk=pk)
        data = ShowroomSerializer(dealer_detail).data
        return Response({"Showroom details": data}, status=status.HTTP_200_OK)

    @action(methods=["post"], url_path="create", detail=False)
    def create_showroom(self, request):
        dealer_serializer = ShowroomSerializer(data=request.data)
        dealer_serializer.is_valid(raise_exception=True)
        dealer_serializer.save()
        data = dealer_serializer.data
        return Response({"New dealer detail": data}, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=["delete"], permission_classes=[AllowAny], url_path="delete")
    def delete(self, request, pk):
        return super(ShowroomsViewSet, self).delete(request, pk)
