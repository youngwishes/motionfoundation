from rest_framework import viewsets
from .serializers import ActivitySerializer, ActivityTypeSerializer
from rest_framework import permissions
from dvizhenie.core.loading import get_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter


__all__ = ['ActivityViewSet', 'ActivityTypeViewSet']


Activity = get_model('activities', 'Activity')
ActivityType = get_model('activities', 'ActivityType')


class ActivityViewSet(viewsets.ModelViewSet):
    """
    API endpoint allows activities to be viewed or edited
    """
    queryset = Activity.objects.select_related('activity_type').prefetch_related('files')
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['activity_type']
    ordering_fields = ['name', 'activity_type']


class ActivityTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint allows activities to be viewed or edited
    """
    queryset = ActivityType.objects.all().order_by('name')
    serializer_class = ActivityTypeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [OrderingFilter]
    ordering_fields = ['name']
