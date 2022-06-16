from django_filters import rest_framework as filters

from .models import Car, Dealer


class DealerFilter(filters.FilterSet):
    class Meta:
        model = Dealer
        fields = {"name": ["iexact"], "email": ["iexact"]}
