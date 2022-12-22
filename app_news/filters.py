from django_filters import FilterSet, NumberFilter
from dvizhenie.core.loading import get_model


News = get_model('news', 'News')


class NewsFilter(FilterSet):
    month = NumberFilter(field_name='created_at', lookup_expr='month')
    year = NumberFilter(field_name='created_at', lookup_expr='year')

    class Meta:
        model = News
        fields = ['month', 'year']
