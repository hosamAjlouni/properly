import django_filters
from django_filters import DateRangeFilter, RangeFilter
from django_filters.widgets import RangeWidget
from .models import Lease

class LeaseFilter(django_filters.FilterSet):
    class Meta:
        model   = Lease
        fields  = '__all__'
        exclude = ['user', 'start', 'end']