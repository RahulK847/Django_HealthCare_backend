"""
URL configuration for healthcare_backend project.

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
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from . import views

# Swagger schema view
schema_view = get_schema_view(
    openapi.Info(
        title="Healthcare Backend API",
        default_version='v1',
        description="""
        🏥 **Healthcare Management System API**
        
        A comprehensive REST API for healthcare management built with Django REST Framework.
        
        **Features:**
        - JWT Authentication
        - User Management (Patient/Doctor roles)
        - Patient CRUD Operations
        - Doctor Management
        - Patient-Doctor Mapping
        
        **Authentication:**
        Use the 'Authorize' button below to add your Bearer token for protected endpoints.
        
        **Created by:** Rahul Kumar
        - GitHub: https://github.com/RahulK847
        - Portfolio: https://www.rahulk847.live/
        """,
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="rahul@example.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Swagger Documentation
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    
    # Health check and admin
    path('health/', views.health_check, name='health_check'),  
    path('admin/', admin.site.urls),
    
    # API endpoints
    path('api/auth/', include('users.urls')),
    path('api/patients/', include('patients.urls')),
    path('api/doctors/', include('doctors.urls')),
    path('api/mappings/', include('mappings.urls')),
]
