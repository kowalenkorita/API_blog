from rest_framework import serializers

from api.models import News

__all__ = (
    'NewsSerializer',
)


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        read_only_fields = (
            'id',
        )
        model = News
