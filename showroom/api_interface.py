from core.common_api_interface.common_api_interface import CustomViewSet
from core.permissions.permissions import IsShowroomUser
from rest_framework import permissions, status
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response

from .models import Showroom
from .serializers import MainShowroomSerializer


class ShowroomsViewSet(CustomViewSet):
    queryset = Showroom.objects.all()
    serializer_class = MainShowroomSerializer()
    permission_classes = [IsAdminUser, IsShowroomUser]
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ("name",)
    # filterset_class = ShowroomFilter

    @action(methods=["get"], detail=False, url_path="list")
    def list_of_showrooms(self, request):
        return super(ShowroomsViewSet, self).get(request)

    @action(methods=["get"], detail=True, url_path="details")
    def detail_of_showroom(self, request, pk):
        showroom_detail = Showroom.objects.get(pk=pk)
        data = MainShowroomSerializer(showroom_detail).data
        return Response({"Showroom details": data}, status=status.HTTP_200_OK)

    @action(methods=["post"], url_path="create", detail=False)
    def create_showroom(self, request):
        return super(MainShowroomSerializer, self).post(request)

    @action(
        detail=True,
        methods=["delete"],
        permission_classes=[AllowAny],
        url_path="delete",
    )
    def delete(self, request, pk):
        return super(ShowroomsViewSet, self).delete(request, pk)
