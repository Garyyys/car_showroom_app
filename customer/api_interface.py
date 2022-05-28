from rest_framework import viewsets, permissions
from .models import CustomerOrder
from .serializers import CustomerOrderSerializer
from .filters import CustomerFilter


class CustomerViewSet(viewsets.ModelViewSet):
    """
       A viewset for information about customers and theirs orders
    """

    queryset = CustomerOrder.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CustomerOrderSerializer
    filterset_class = CustomerFilter
