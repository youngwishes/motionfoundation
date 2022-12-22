from rest_framework import viewsets
from dvizhenie.core.loading import get_model
from .serializers import *
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter


AboutTheFund = get_model('root', 'AboutTheFund')
Contacts = get_model('root', 'Contacts')
File = get_model('root', 'File')


class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['is_fond_doc']
    ordering_fields = ['capture']


class ContactsViewSet(viewsets.ModelViewSet):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AboutTheFundViewSet(viewsets.ModelViewSet):
    queryset = AboutTheFund.objects.all()
    serializer_class = AboutTheFundSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


