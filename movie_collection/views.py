from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404

from .models import Movie
from .forms import MovieForm


def index(request):
    return render(request, 'index.html')


def movie_list(request):
    return render(request, 'movie_list.html', {
        'movies': Movie.objects.all(),
    })


def add_movie(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            messages.success(request, f"{movie.title} added.")
            return HttpResponse(
                headers={
                    'HX-Trigger': '{"movieListChanged":true,"closeModal":true}',
                    'HX-Reswap': "none",
                }
            )
    else:
        form = MovieForm()
    return render(request, 'movie_form.html', {
        'form': form,
    })


def edit_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "POST":
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            messages.success(request, f"{movie.title} updated.")
            return HttpResponse(
                headers={
                    'HX-Trigger': '{"movieListChanged":true,"closeModal":true}',
                    'HX-Reswap': "none",
                }
            )
    else:
        form = MovieForm(instance=movie)
    return render(request, 'movie_form.html', {
        'form': form,
        'movie': movie,
    })


@ require_POST
def remove_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    movie.delete()
    messages.success(request, f"{movie.title} deleted.")
    return HttpResponse(
        headers={
            'HX-Trigger': '{"movieListChanged":true,"closeModal":true}',
            'HX-Reswap': "none",
        }
    )
