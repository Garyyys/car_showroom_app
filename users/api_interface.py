import json

import requests
from core.common_api_interface.common_api_interface import CustomViewSet
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from users.models import ShowroomUser
from users.serializers import ShowroomUserSerializer


class ShowroomUserViewSet(CustomViewSet):
    queryset = ShowroomUser.objects.all()
    serializer_class = ShowroomUserSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ("username",)

    @action(
        detail=False,
        methods=["get"],
        permission_classes=[AllowAny],
        url_path="list",
    )
    def get(self, request):
        return super(ShowroomUserViewSet, self).get(request)

    @action(
        methods=["get"],
        detail=False,
        permission_classes=[AllowAny],
        url_path=r"activate/(?P<uid>[\w-]+)/(?P<token>[\w-]+)",
    )
    def activate_user_account(self, request, uid, token):
        protocol = "https://" if request.is_secure() else "http://"
        web_url = protocol + request.get_host()
        post_url = web_url + "/api/auth/users/activation/"
        post_data = {"uid": uid, "token": token}
        result = requests.post(post_url, data=post_data)
        content = "Registration completed successfully"
        return Response(content)

    @action(
        ["get"],
        detail=True,
        permission_classes=[AllowAny],
        url_path="details",
    )
    def get_details(self, request, pk):
        pass

    @action(
        detail=False,
        permission_classes=[AllowAny],
        methods=["post"],
        url_path="create",
    )
    def post(self, request):
        return super(ShowroomUserViewSet, self).post(request)

    @action(
        detail=True,
        methods=["put"],
        permission_classes=[AllowAny],
        url_path="update",
    )
    def put(self, request, pk=None):
        return super(ShowroomUserViewSet, self).put(request, pk)

    @action(
        detail=True,
        methods=["delete"],
        permission_classes=[AllowAny],
        url_path="delete",
    )
    def delete(self, request, pk):
        return super(ShowroomUserViewSet, self).delete(request, pk)
