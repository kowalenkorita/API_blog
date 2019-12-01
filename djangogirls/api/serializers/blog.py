from rest_framework import serializers

from api.models import Blog

__all__ = (
    'BlogSerializer',
)


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        read_only_fields = (
            'id',
        )
        model = Blog
