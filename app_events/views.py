from rest_framework import viewsets
from .seralizers import EventSerializer, AddressSerializer
from dvizhenie.core.loading import get_model
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .filters import EventsFilter


__all__ = ['EventViewSet', 'AddressViewSet']


FundEvent = get_model('events', 'FundEvent')
Address = get_model('events', 'Address')


class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint allows events to be viewed or edited
    """
    queryset = FundEvent.objects.prefetch_related('files', 'addresses').order_by('start_timestamp')
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = EventsFilter
    ordering_fields = ['start_timestamp', 'end_timestamp']


class AddressViewSet(viewsets.ModelViewSet):
    """
    API endpoint allows addresses to be viewed or edited
    """
    queryset = Address.objects.all().order_by('address')
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
