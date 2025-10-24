from django.urls import path
from .blog import post_list
from .menu import menu

urlpatterns = [
    path('menu/list', menu),
    path('blog/post/list', post_list),
]
