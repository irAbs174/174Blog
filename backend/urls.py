"""
URL configuration for 174Blog project.
"""
from django.contrib import admin
from django.urls import path
from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index)
]
