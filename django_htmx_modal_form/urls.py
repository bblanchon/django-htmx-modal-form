from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from movie_collection import views
from urllib.parse import urlparse

MEDIA_PATH = urlparse(settings.MEDIA_URL).path

urlpatterns = [
    path('', views.index),
    path('movies', views.movie_list, name='movie_list'),
    path('movies/add', views.add_movie, name='add_movie'),
    path('movies/<int:pk>/remove', views.remove_movie, name='remove_movie'),
    path('movies/<int:pk>/edit', views.edit_movie, name='edit_movie'),
] + static(MEDIA_PATH, document_root=settings.MEDIA_ROOT)
