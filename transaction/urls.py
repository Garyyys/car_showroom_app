from django.urls import path, include
from rest_framework import routers
from .api_interface import TransactionViewSet, DiscountViewSet

router = routers.DefaultRouter()
router.register(r'transaction', TransactionViewSet, 'transaction')
router.register(r'discount', DiscountViewSet, 'discount')

urlpatterns = [
    path('', include(router.urls))
]
