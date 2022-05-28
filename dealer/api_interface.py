from rest_framework import viewsets, permissions, status
from .models import DealerCarForSale, Car
from .serializers import DealerCarForSaleSerializer, CarSerializer
from .filters import DealerFilter, CarFilter


class DealerViewSet(viewsets.ModelViewSet):
    """
        A viewset for information about suppliers and theirs cars
    """

    queryset = DealerCarForSale.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = DealerCarForSaleSerializer
    filterset_class = DealerFilter


class CarViewSet(viewsets.ModelViewSet):
    """
        A viewset for information about cars
    """

    queryset = Car.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CarSerializer
    filterset_class = CarFilter
