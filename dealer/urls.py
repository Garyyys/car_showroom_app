from django.urls import include, path
from rest_framework import routers

from .api_interface import CarViewSet, DealerViewSet

router = routers.DefaultRouter()
router.register(r"dealer", DealerViewSet)
router.register(r"car", CarViewSet)
# print('ROUTS!!!', router.urls)
urlpatterns = [path("", include(router.urls))]
