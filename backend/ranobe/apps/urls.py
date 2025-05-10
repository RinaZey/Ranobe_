from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Ranobe API",
        default_version="v1",
        description="Ranobe v1 API",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)

docs_patterns = [
    path('',  schema_view.with_ui(
        'swagger', cache_timeout=0), name='schema-swagger-ui'),
]

urlpatterns = [
    path('documentation/', include((docs_patterns, 'docs'), 'docs')),

    path('ranobes/', include(('apps.ranobes.urls', 'ranobes'), 'ranobes')),

    path('metadata/', include(('apps.metadata.urls', 'metadata'), 'metadata')),
]
