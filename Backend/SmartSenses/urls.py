"""SmartSenses URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from cuentas import views as users_views
from dispositivos import views as devices_views
from lecturas import views as readings_views
from alertas import views as alerts_views


# Routers para cada aplicación
users_router = routers.DefaultRouter() 
users_router.register(r'', users_views.UserView, basename='users')

devices_router = routers.DefaultRouter() 
devices_router.register(r'', devices_views.DeviceView, basename='devices')

readings_router = routers.DefaultRouter() 
readings_router.register(r'', readings_views.ReadingView, basename='readings')

alerts_router = routers.DefaultRouter() 
alerts_router.register(r'', alerts_views.AlertView, basename='alerts')


urlpatterns = [
    # Enrutado de API para cada aplicación
    path('admin/', admin.site.urls),
    path('api/v1/users/', include(users_router.urls)),
    path('api/v1/devices/', include(devices_router.urls)),
    path('api/v1/readings/', include(readings_router.urls)),
    path('api/v1/alerts/', include(alerts_router.urls)),

    # Documentación global para la API
    path("api/v1/docs/", include_docs_urls(title="API Documentation")),
]
