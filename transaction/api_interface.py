from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import SalesShowroomToCustomer, SalesDealerToShowroom
from showroom.models import DiscountShowroom
from showroom.serializers import DiscountShowroomSerializer
from dealer.models import DiscountDealer
from dealer.serializers import DiscountDealerSerializer
from .serializers import SalesShowroomToBuyersSerializer, SalesDealerToShowroomSerializer


class TransactionViewSet(viewsets.ViewSet):
    """
       A viewset for sales between showrooms-buyers and suppliers-showrooms
    """

    def list(self):
        sales_showroom_customer = SalesShowroomToCustomer.objects.all()
        sales_dealer_showrooms = SalesDealerToShowroom.objects.all()
        serializer_sh_customer = SalesShowroomToBuyersSerializer(sales_showroom_customer, many=True)
        serializer_de_showroom = SalesDealerToShowroomSerializer(sales_dealer_showrooms, many=True)
        serializer_dict = {
            "sales_showroom_buyers": serializer_sh_customer.data,
            "sales_suppliers_showrooms": serializer_de_showroom.data,
        }
        return Response(serializer_dict, status=status.HTTP_200_OK)


class DiscountViewSet(viewsets.ViewSet):
    """
    A viewset for discounts of showrooms and suppliers
    """

    def list(self):
        discounts_showrooms = DiscountShowroom.objects.all()
        discounts_dealer = DiscountDealer.objects.all()
        serializer_discounts_showrooms = DiscountShowroomSerializer(discounts_showrooms, many=True)
        serializer_discounts_dealer = DiscountDealerSerializer(discounts_dealer, many=True)
        serializer_dict = {
            "discounts_showrooms": serializer_discounts_showrooms.data,
            "discounts_dealer": serializer_discounts_dealer.data,
        }
        return Response(serializer_dict, status=status.HTTP_200_OK)
