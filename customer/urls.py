from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from customer.api_interface import (
    CustomerListAPIView,
    CustomerOrderViewSet,
    get_details,
    get_orders,
)

urlpatterns = [
    path("customer/", CustomerListAPIView.as_view()),
    path("customer/order/", CustomerOrderViewSet.as_view()),
    path("customer/details/<int:pk>", get_details),
    path("customer/orders/<int:pk>", get_orders),
]

urlpatterns = format_suffix_patterns(urlpatterns)
