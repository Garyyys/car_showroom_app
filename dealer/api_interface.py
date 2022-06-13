from core.common_api_interface.common_api_interface import CustomViewSet
from core.permissions.permissions import IsDealerUser, IsShowroomUser
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .filters import CarFilter, DealerFilter
from .models import Car, Dealer
from .serializers import CarSerializer, DealerSerializer


# TODO: make permissions
class DealerViewSet(CustomViewSet):
    """
    A viewset for information about suppliers and theirs cars
    """

    # TODO: add permissions and filter sets
    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer
    permission_classes = [IsAdminUser, IsDealerUser]
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ("name",)

    @action(methods=["get"], detail=False, url_path="list")
    def list_of_dealers(self, request):
        return super(DealerViewSet, self).get(request)

    @action(methods=["get"], detail=True, url_path="details")
    def detail_of_dealer(self, request, pk):
        dealer_detail = Dealer.objects.get(pk=pk)
        data = DealerSerializer(dealer_detail).data
        return Response({"dealer details": data}, status=status.HTTP_200_OK)

    @action(methods=["post"], url_path="create", detail=False)
    def create_dealer(self, request):
        return super(DealerViewSet, self).post(request)

    # TODO: remake function, do not delete instance, change is_active field to False
    @action(detail=True, methods=["delete"], url_path="delete")
    def delete(self, request, pk):
        return super(DealerViewSet, self).delete(request, pk)
