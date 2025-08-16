"""
URL configuration for Todo_list project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

from drf_yasg import openapi  as drf_yasg_openapi
from drf_yasg import views as drf_yasg_views
from rest_framework import permissions
from rest_framework.schemas import get_schema_view


schema_view = drf_yasg_views.get_schema_view(
    drf_yasg_openapi.Info(
        title='ToDo API',
        default_version = "v1",
        descrtiption = "ToDo API",
        contact = drf_yasg_openapi.Contact(email='info.mukhammadmirzo078@gmail.com'),
        license=drf_yasg_openapi.License(name="Proprietary software license")
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('todos.urls')),
    
    #Swagger 
    # Swagger
path("schema/", get_schema_view(
    title="API's",
    description="API for Erp contract",
), name="openapi-schema"),

path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
path("swagger/json/", schema_view.without_ui(cache_timeout=0), name="schema-json"),
path("swagger/yaml/", schema_view.without_ui(cache_timeout=0), name="schema-yaml"),

]
