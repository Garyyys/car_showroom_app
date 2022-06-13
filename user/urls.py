from django.urls import include, path
from rest_framework import routers

from user.api_interface import ShowroomUserViewSet

router = routers.DefaultRouter()
router.register(r"user", ShowroomUserViewSet)

urlpatterns = [path("", include(router.urls))]
