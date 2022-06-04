from django.urls import include, path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from .api_interface import CustomerListAPIView

urlpatterns = [
    path("customer/", CustomerListAPIView.as_view()),
    path("customer/<int:pk>", CustomerListAPIView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
