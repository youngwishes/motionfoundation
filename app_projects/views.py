from rest_framework import viewsets
from .serializers import PartnerSerializer, ProjectSerializer
from dvizhenie.core.loading import get_model
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter


__all__ = ['ProjectViewSet', 'PartnerViewSet']


Project = get_model('projects', 'Project')
Partner = get_model('projects', 'Partner')


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.prefetch_related('files', 'partners')
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['is_finished']
    ordering_fields = ['start_timestamp', 'end_timestamp', 'name']


class PartnerViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
