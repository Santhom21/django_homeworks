import django_filters
from advertisements.models import Advertisement

class AdvertisementFilter(django_filters.FilterSet):
    """Фильтры для объявлений."""

    created_at = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ('created_at', 'status',)
