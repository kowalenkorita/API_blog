from django.urls import (
    include,
    path,
)
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(openapi.Info(title='API',
                                           default_version='v1'))

urlpatterns = [
    path('api/<str:version>/', include('api.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema_swagger'),
]
