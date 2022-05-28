from rest_framework import viewsets, permissions
from .models import ShowroomCarForSale
from .serializers import ShowroomCarForSaleSerializer
from .filters import ShowroomsFilter


class ShowroomsViewSet(viewsets.ModelViewSet):
    """
       A viewset for information about showrooms and theirs cars
    """

    queryset = ShowroomCarForSale.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ShowroomCarForSaleSerializer
    filterset_class = ShowroomsFilter
