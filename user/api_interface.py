from core.common_api_interface.common_api_interface import CustomViewSet
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from user.models import ShowroomUser
from user.serializers import ShowroomUserSerializer


class ShowroomUserViewSet(CustomViewSet):
    queryset = ShowroomUser.objects.all()
    serializer_class = ShowroomUserSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ("username",)

    @action(
        detail=False,
        methods=["get"],
        permission_classes=[IsAuthenticated],
        url_path="list",
    )
    def get(self, request):
        return super(ShowroomUserViewSet, self).get(request)

    @action(
        ["get"],
        detail=True,
        permission_classes=[
            IsAdminUser,
        ],
        url_path="details",
    )
    def get_details(self, request, pk):
        pass

    @action(
        detail=False,
        permission_classes=[IsAdminUser],
        methods=["post"],
        url_path="create",
    )
    def post(self, request):
        return super(ShowroomUserViewSet, self).post(request)

    @action(
        detail=True,
        methods=["put"],
        permission_classes=[IsAdminUser],
        url_path="update",
    )
    def put(self, request, pk=None):
        return super(ShowroomUserViewSet, self).put(request, pk)

    @action(
        detail=True,
        methods=["delete"],
        permission_classes=[IsAdminUser],
        url_path="delete",
    )
    def delete(self, request, pk):
        return super(ShowroomUserViewSet, self).delete(request, pk)
