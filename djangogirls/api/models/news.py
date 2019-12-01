from django.db import models

__all__ = (
    'News',
)


class News(models.Model):
    title = models.TextField()
    content = models.TextField()
    url = models.URLField(null=True, blank=True)

    blog_id = models.ForeignKey('Blog', on_delete=models.CASCADE)
