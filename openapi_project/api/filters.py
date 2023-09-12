import django_filters
from .models import Cinemas

class CinemasFilter(django_filters.FilterSet):
    class Meta:
        model = Cinemas
        fields = {
            'cinema_name': ['icontains'],
            'address': ['icontains'],
            'description': ['icontains'],
        }
