from django_filters import rest_framework as filters
from rest_framework import mixins, permissions, status, viewsets
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from core.common_views.views import CustomViewSet

from .filters import CarFilter, DealerFilter
from .models import Car, Dealer, DealerCarForSale
from .serializers import CarSerializer, DealerCarForSaleSerializer, DealerSerializer


@permission_classes(
    [
        permissions.AllowAny,
    ]
)
class DealerViewSet(CustomViewSet):
    """
    A viewset for information about suppliers and theirs cars
    """

    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer
    filterset_class = DealerFilter

    @action(methods=["get"], detail=False, url_path="list")
    def list_of_dealers(self, request):
        dealers = Dealer.objects.all()
        return Response({"dealers": DealerSerializer(dealers, many=True).data})

    @action(methods=["get"], detail=True, url_path="details")
    def detail_of_dealer(self, request, pk):
        dealer_detail = Dealer.objects.get(pk=pk)
        return Response(
            {"dealer details": DealerSerializer(dealer_detail, many=False).data},
            status=status.HTTP_200_OK,
        )

    @action(methods=["post"], url_path="create", detail=False)
    def create_dealer(self, request):
        dealer_serializer = DealerSerializer(data=request.data)
        dealer_serializer.is_valid(raise_exception=True)
        dealer_serializer.save()
        return Response(
            {"New dealer detail": dealer_serializer.data},
            status=status.HTTP_201_CREATED,
        )

    @action(
        detail=True,
        methods=["delete"],
        permission_classes=[AllowAny],
        url_name="delete",
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
