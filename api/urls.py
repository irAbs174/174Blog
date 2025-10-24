from django.urls import path
from .blog import post_list

urlpatterns = [
    path('blog/post/list', post_list),
]
