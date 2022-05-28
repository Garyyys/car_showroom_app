from django_filters import rest_framework as filters
from .models import ShowroomCarForSale


class ShowroomsFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="showroom__name", lookup_expr="icontains")
    is_available = filters.BooleanFilter(field_name="showroom__is_available", lookup_expr="exact")
    email = filters.CharFilter(field_name="showroom__email", lookup_expr="exact")
    added_date = filters.DateFilter(field_name="showroom__added_date", lookup_expr="exact")
    date_updated = filters.DateFilter(field_name="showroom__date_updated", lookup_expr="exact")
    brand = filters.CharFilter(field_name="car__brand", lookup_expr="exact")
    model = filters.CharFilter(field_name="car__model", lookup_expr="exact")
    color = filters.CharFilter(field_name="car__color", lookup_expr="exact")
    year = filters.NumberFilter(field_name="car__year", lookup_expr="exact")
    body_type = filters.CharFilter(field_name="car__body_type", lookup_expr="exact")
    price_range = filters.NumericRangeFilter(field_name="price", lookup_expr="exact")
    price_exact = filters.NumberFilter(field_name="price", lookup_expr="exact")
    cars_count = filters.NumberFilter(field_name="cars_count", lookup_expr="exact")

    class Meta:
        model = ShowroomCarForSale
        fields = ()