from django_filters import FilterSet, NumberFilter, BooleanFilter
from dvizhenie.core.loading import get_model


FundEvent = get_model('events', 'FundEvent')


class EventsFilter(FilterSet):
    month = NumberFilter(field_name='start_timestamp', lookup_expr='month')
    year = NumberFilter(field_name='start_timestamp', lookup_expr='year')
    is_online = BooleanFilter('is_online', lookup_expr='exact')

    class Meta:
        model = FundEvent
        fields = ['month', 'year', 'is_online']
