from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="API for Cinemas Open Data",
        default_version='v1',
        description="API on Django, that uses django-rest-framework "
                    "technology for providing opportunity to view information "
                    "about cinemas in Russia. The api also makes possible "
                    "to filter results by words in various fields (by using search), or to make "
                    "strict filter using one or several fields. "
                    "To see the output of all info oor to do other described actions,"
                    "you should follow link http://127.0.0.1:8000/api/cinemas/",
        # terms_of_service="",
        # contact=openapi.Contact(email="contact@yourapp.com"),
        # license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
