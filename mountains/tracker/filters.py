import django_filters
from django_filters import CharFilter, DateFilter
from .models import Mountain, Hike

class MountainFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    less_than_height = CharFilter(field_name='height', lookup_expr='lt')
    greater_than_height = CharFilter(field_name='height', lookup_expr='gt')
    notes = CharFilter(field_name='notes', lookup_expr='icontains')
    start_date = DateFilter(field_name='date_climbed', lookup_expr='gte', label='Climbed after (YYYY-MM-DD)')
    end_date = DateFilter(field_name='date_climbed', lookup_expr='lte', label='Climbed before (YYYY-MM-DD)')
    
    class Meta:
        model = Mountain
        fields = '__all__'
        exclude = ['height', 'date_climbed', 'longitude', 'latitude', 'featured_image']

class HikeFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    less_than_length = CharFilter(field_name='length', lookup_expr='lt')
    greater_than_length = CharFilter(field_name='length', lookup_expr='gt')
    notes = CharFilter(field_name='notes', lookup_expr='icontains')
    start_date = DateFilter(field_name='hike_date', lookup_expr='gte', label='Hike after (YYYY-MM-DD)')
    end_date = DateFilter(field_name='hike_date', lookup_expr='lte', label='Hike before (YYYY-MM-DD)')
    less_than_duration = CharFilter(field_name='duration', lookup_expr='lt')
    greater_than_duration = CharFilter(field_name='duration', lookup_expr='gt')

    class Meta:
        model = Hike
        fields = '__all__'
        exclude = ['duration', 'total_ascent', 'total_descent', 'featured_image']