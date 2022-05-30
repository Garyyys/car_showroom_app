from rest_framework.response import Response
from rest_framework import viewsets, permissions
from rest_framework.decorators import action

from .models import CustomerOrder, Customer
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

    @action(methods=['get'], detail=False)
    def customerlist(self, request):
        cr = Customer.objects.all()
        return Response({'cr': [c.name for c in cr]})
