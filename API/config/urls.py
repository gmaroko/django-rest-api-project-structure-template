from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Application Title",
        default_version='beta',
        description="Application Description",
        terms_of_service="https://www.google.com/policies/terms/", # link to your terms of service
        contact=openapi.Contact(email="marokogiedeon@gmail.com"), # contacts
        license=openapi.License(name="BSD License"), #license type
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    # django admin
    path('secret/', admin.site.urls),

    # api endpoints
    path('api/', include('API.apps.authentication.urls', namespace='authentication')),
    # path('api/', include('API.apps.profiles.urls', namespace='profiles')),

    # api documentation
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
