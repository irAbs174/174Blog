"""
URL configuration for 174Blog project.
"""
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from .views import index

urlpatterns = [
    path('api/', include("api.urls") ),
    path('admin/', admin.site.urls),
    path('', index),
]

# Serve static files in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)