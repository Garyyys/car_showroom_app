from django_filters import rest_framework as filters

from .models import Car, Dealer


class DealerFilter(filters.FilterSet):
    class Meta:
        model = Dealer
        fields = {
            "name": ["iexact"],
            "email": ["iexact"],
            "make": ["iexact"],
            "model": ["iexact"],
        }

    class Meta:
        model = Dealer
        fields = ()


class CarFilter(filters.FilterSet):
    make = filters.CharFilter(field_name="make", lookup_expr="icontains")
    model = filters.CharFilter(field_name="model", lookup_expr="icontains")
    color = filters.CharFilter(field_name="color", lookup_expr="exact")
    year = filters.NumberFilter(field_name="year", lookup_expr="exact")
    engine = filters.NumberFilter(field_name="engine", lookup_expr="exact")
    body_type = filters.CharFilter(field_name="brand", lookup_expr="exact")
    added_date = filters.DateFilter(field_name="added_date", lookup_expr="exact")

    class Meta:
        model = Car
        fields = (
            "make",
            "model",
            "color",
            "year",
            "engine",
            "body_type",
            "added_date",
        )
