from rest_framework.routers import DefaultRouter

from api.viewsets import (
    BlogViewSet,
    NewsViewSet,
)

router = DefaultRouter()
router.register('blogs', BlogViewSet, basename='blog')
router.register('news', NewsViewSet, basename='news')
urlpatterns = router.urls
