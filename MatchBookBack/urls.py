from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="MatchBook API",
        default_version='v1',
        description="MatchBook API",
        terms_of_service="https://www.google.com/policies/terms/",    
    )
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/authentication/', include('authentication.urls')),
    re_path(r'^swagger/$', schema_view.with_ui('swagger')),

]
