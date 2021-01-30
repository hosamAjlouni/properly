import django_filters
from django_filters.widgets import RangeWidget
from django_filters import NumericRangeFilter, RangeFilter
from .models import Unit


class UnitFilter(django_filters.FilterSet):
    class Meta:
        model   = Unit
        fields  = ['property', 'num', 'deposit', 'beds', 'baths']
        exclude = ['user', 'market_rent', 'description']

    market_rent     = NumericRangeFilter(field_name='market_rent', lookup_expr='range', label='Price Range')
    size            = NumericRangeFilter(field_name='size', lookup_expr='range', label='Size Range')
    vacant_in       = RangeFilter(field_name='property', label='Vacant in', widget=RangeWidget(attrs={'type': 'date'}))

        