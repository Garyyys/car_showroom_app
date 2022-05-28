from django_filters import rest_framework as filters
from .models import SalesShowroomToCustomer, SalesDealerToShowroom


class SalesShowroomToCustomerFilter(filters.FilterSet):
    id_buyer = filters.NumberFilter(field_name="id_buyer", lookup_expr="exact")
    id_showroom = filters.NumberFilter(field_name="id_showroom", lookup_expr="exact")
    id_car = filters.NumberFilter(field_name="id_car", lookup_expr="exact")
    price = filters.NumberFilter(field_name="price", lookup_expr="exact")
    amount_of_discount = filters.NumberFilter(field_name="amount_of_discount", lookup_expr="exact")
    added_date = filters.DateFilter(field_name="added_date", lookup_expr="exact")

    class Meta:
        model = SalesShowroomToCustomer
        fields = ('id_buyer', 'id_showroom', 'id_car', 'price', 'amount_of_discount', 'added_date')


class SalesDealerToShowroomFilter(filters.FilterSet):
    id_dealer = filters.NumberFilter(field_name="id_dealer", lookup_expr="exact")
    id_showroom = filters.NumberFilter(field_name="id_showroom", lookup_expr="exact")
    id_car = filters.NumberFilter(field_name="id_car", lookup_expr="exact")
    price = filters.NumberFilter(field_name="price", lookup_expr="exact")
    amount_of_discount = filters.NumberFilter(field_name="amount_of_discount", lookup_expr="exact")
    added_date = filters.DateFilter(field_name="added_date", lookup_expr="exact")

    class Meta:
        model = SalesDealerToShowroom
        fields = ('id_dealer', 'id_showroom', 'id_car', 'price', 'amount_of_discount', 'added_date')