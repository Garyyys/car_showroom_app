from django.urls import include, path
from rest_framework import routers

from transaction.api_interface import (
    TransactionDealerToShowroomViewSet,
    TransactionShowroomToCustomerViewSet,
)

router = routers.DefaultRouter()
router.register(r"transaction/showroom", TransactionShowroomToCustomerViewSet)
router.register(r"transaction/dealer", TransactionDealerToShowroomViewSet)

urlpatterns = [path("", include(router.urls))]
