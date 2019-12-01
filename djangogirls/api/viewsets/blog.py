from rest_framework import viewsets

from api.models import Blog
from api.serializers import BlogSerializer

__all__ = (
    'BlogViewSet',
)


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
