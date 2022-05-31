from django_filters import rest_framework as filters
from .models import DealerCarForSale, Car


class DealerFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="supplier__name", lookup_expr="icontains")
    found_year = filters.NumberFilter(field_name="supplier__year_of_foundation", lookup_expr="exact")
    number_of_buyers = filters.NumberFilter(field_name="dealer__found_year", lookup_expr="icontains")
    is_available = filters.BooleanFilter(field_name="supplier__is_available", lookup_expr="exact")
    email = filters.CharFilter(field_name="supplier__email", lookup_expr="exact")
    added_date = filters.DateFilter(field_name="supplier__added_date", lookup_expr="exact")
    date_updated = filters.DateFilter(field_name="supplier__date_updated", lookup_expr="exact")
    make = filters.CharFilter(field_name="car__make", lookup_expr="exact")
    model = filters.CharFilter(field_name="car__model", lookup_expr="exact")
    color = filters.CharFilter(field_name="car__color", lookup_expr="exact")
    year = filters.NumberFilter(field_name="car__year", lookup_expr="exact")
    body_type = filters.CharFilter(field_name="car__body_type", lookup_expr="exact")
    price_range = filters.NumericRangeFilter(field_name="price", lookup_expr="exact")
    price_exact = filters.NumberFilter(field_name="price", lookup_expr="exact")

    class Meta:
        model = DealerCarForSale
        fields = ()


class CarFilter(filters.FilterSet):
    make = filters.CharFilter(field_name="make", lookup_expr="icontains")
    model = filters.CharFilter(field_name="model", lookup_expr="icontains")
    color = filters.CharFilter(field_name="color", lookup_expr="exact")
    year = filters.NumberFilter(field_name="year", lookup_expr="exact")
    engine = filters.NumberFilter(field_name="engine", lookup_expr="exact")
    body_type = filters.CharFilter(field_name="brand", lookup_expr="exact")
    added_date = filters.DateFilter(field_name="added_date", lookup_expr="exact")
    date_updated = filters.DateFilter(field_name="date_updated", lookup_expr="exact")

    class Meta:
        model = Car
        fields = ('make', 'model', 'color', 'year', 'engine', 'body_type', 'added_date')
