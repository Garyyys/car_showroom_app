from django.urls import path, include
from rest_framework import routers
from .api_interface import CustomerViewSet, CustomerListAPIView

router = routers.DefaultRouter()
router.register(r'customer', CustomerViewSet)


print('ROUTS!!!', router.urls)

urlpatterns = [
    path('', include(router.urls)),
    path('crlist/', CustomerListAPIView.as_view()),
    path('crlist/<int:pk>', CustomerListAPIView.as_view()),
]
