from django_filters import rest_framework as filters
from django_filters.rest_framework import FilterSet

from .models import SalesDealerToShowroom, SalesShowroomToCustomer


class ShowroomToCustomerFilter(FilterSet):
    model = SalesShowroomToCustomer
    fields = {
        "car__make": ["iexact"],
        "car__model": ["iexact"],
        "customer__name": ["iexact"],
        "showroom__name": ["iexact"],
        "price": ["exact", "lt", "gt"],
        "added_date": ["exact", "lt", "gt"],
    }


class DealerToShowroomFilter(FilterSet):
    model = SalesDealerToShowroom
    fields = {
        "car__make": ["iexact"],
        "car__model": ["iexact"],
        "dealer__name": ["iexact"],
        "showroom__name": ["iexact"],
        "price": ["exact", "lt", "gt"],
        "added_date": ["exact", "lt", "gt"],
    }
