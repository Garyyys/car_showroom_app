from rest_framework import status
from rest_framework.response import Response
from django_filters import rest_framework as filters
from core.common_views.views import CustomViewSet
from rest_framework import viewsets, status, mixins, permissions
from rest_framework.decorators import action, permission_classes
from .models import DealerCarForSale, Car, Dealer
from .serializers import DealerCarForSaleSerializer, CarSerializer, \
    DealerSerializer
from .filters import DealerFilter, CarFilter


@permission_classes([permissions.AllowAny, ])
class DealerViewSet(CustomViewSet):
    """
        A viewset for information about suppliers and theirs cars
    """
    queryset = DealerCarForSale.objects.all()
    serializer_class = DealerCarForSaleSerializer
    filter_backends = filters.DjangoFilterBackend
    filterset_class = DealerFilter

    @action(methods=['get'], detail=False, url_path='list')
    def list_of_dealers(self, request):
        dealers = Dealer.objects.all()
        return Response({'dealers': DealerSerializer(dealers, many=True).data})

    @action(methods=['get'], detail=True, url_path='details')
    def detail_of_dealer(self, request, pk):
        dealer_detail = Dealer.objects.get(pk=pk)
        return Response({'dealer details': DealerSerializer(dealer_detail,
                                                            many=False).data},
                        status=status.HTTP_200_OK)

    @action(methods=['post'], url_path='create', detail=False)
    def create_dealer(self, request):
        dealer_serializer = DealerSerializer(data=request.data)
        dealer_serializer.is_valid(raise_exception=True)
        dealer_serializer.save()
        return Response(
            {'New dealer detail': dealer_serializer.data},
            status=status.HTTP_201_CREATED
        )


class CarViewSet(viewsets.ModelViewSet):
    """
        A viewset for information about cars
    """

    queryset = Car.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CarSerializer
    filterset_class = CarFilter
