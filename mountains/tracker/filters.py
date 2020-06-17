import django_filters
from django_filters import CharFilter
from .models import Mountain

class MountainFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    notes = CharFilter(field_name='notes', lookup_expr='icontains')
    class Meta:
        model = Mountain
        fields = '__all__'
        exclude = ['height', 'date_climbed', 'longitude', 'latitude', 'featured_image']