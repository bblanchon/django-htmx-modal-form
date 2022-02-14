from django.urls import path
from movie_collection import views


urlpatterns = [
    path('', views.index),
    path('movies/add', views.add_movie, name='add_movie'),
    path('movies/<int:pk>/edit', views.edit_movie, name='edit_movie'),
]
