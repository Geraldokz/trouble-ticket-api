from django_filters import rest_framework as filters
from mainapp.models import Event


class EventFilter(filters.FilterSet):
    start_date = filters.DateTimeFromToRangeFilter(field_name='start_date')

    class Meta:
        model = Event
        fields = ['start_date']
