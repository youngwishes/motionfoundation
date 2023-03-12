from rest_framework import viewsets
from .serializers import PartnerSerializer, ProjectSerializer, ProjectTypeSerializer
from dvizhenie.core.loading import get_model
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter


__all__ = ['ProjectViewSet', 'PartnerViewSet', 'ProjectTypeViewSet']


Project = get_model('projects', 'Project')
Partner = get_model('projects', 'Partner')
ProjectType = get_model('projects', 'ProjectType')


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['start_timestamp', 'end_timestamp', 'name']


class PartnerViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProjectTypeViewSet(viewsets.ModelViewSet):
    queryset = ProjectType.objects.all()
    serializer_class = ProjectTypeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
