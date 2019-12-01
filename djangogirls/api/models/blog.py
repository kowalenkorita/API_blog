from django.conf import settings
from django.db import models

__all__ = (
    'Blog',
)


class Blog(models.Model):
    title = models.TextField()
    description = models.TextField()
    
    author_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
