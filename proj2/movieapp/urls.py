# mymovieapp/urls.py
from django.urls import path
from .views import recommend_movie

urlpatterns = [
    path('', recommend_movie, name='recommend_movie'),
]
