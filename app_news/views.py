from .serializers import NewsSerializer
from rest_framework import viewsets
from dvizhenie.core.loading import get_model
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .filters import NewsFilter

News = get_model('news', 'News')


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.prefetch_related('files')
    serializer_class = NewsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['created_at', 'updated_at', 'title']
    filterset_class = NewsFilter
