from rest_framework import viewsets

from api.models import News
from api.serializers import NewsSerializer

__all__ = (
    'NewsViewSet',
)


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
