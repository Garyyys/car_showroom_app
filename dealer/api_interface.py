from core.common_api_interface.common_api_interface import CustomViewSet
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .filters import CarFilter, DealerFilter
from .models import Car, Dealer
from .serializers import CarSerializer, DealerSerializer


# TODO: make permissions
@permission_classes([permissions.AllowAny])
class DealerViewSet(CustomViewSet):
    """
    A viewset for information about suppliers and theirs cars
    """

    # TODO: add permissions and filter sets
    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer
    filterset_class = DealerFilter

    @action(methods=["get"], detail=False, url_path="list")
    def list_of_dealers(self, request):
        dealers = Dealer.objects.all()
        data = DealerSerializer(dealers, many=True).data
        return Response({"dealers": data})

    @action(methods=["get"], detail=True, url_path="details")
    def detail_of_dealer(self, request, pk):
        dealer_detail = Dealer.objects.get(pk=pk)
        data = DealerSerializer(dealer_detail).data
        return Response({"dealer details": data}, status=status.HTTP_200_OK)

    @action(methods=["post"], url_path="create", detail=False)
    def create_dealer(self, request):
        dealer_serializer = DealerSerializer(data=request.data)
        dealer_serializer.is_valid(raise_exception=True)
        dealer_serializer.save()
        data = dealer_serializer.data
        return Response({"New dealer detail": data}, status=status.HTTP_201_CREATED)

    @action(
        detail=True,
        methods=["delete"],
        permission_classes=[AllowAny],
        url_path="delete",
    )
    def delete(self, request, pk):
        return super(DealerViewSet, self).delete(request, pk)


class CarViewSet(viewsets.ModelViewSet):
    """
    A viewset for information about cars
    """

    queryset = Car.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CarSerializer
    filterset_class = CarFilter
