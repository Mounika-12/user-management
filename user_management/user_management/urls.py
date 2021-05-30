"""user_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from users_data import views
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from rest_framework import permissions

schema_view1 = get_schema_view(
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view1.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/?$', schema_view1.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/?$', schema_view1.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    url(r'^users/?$', views.Users_List.as_view()),
    url(r'^users/(?P<pk>\d+)/?$', views.Users_Detail.as_view()),

]
