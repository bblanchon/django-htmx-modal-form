from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

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
            form.save()
            return HttpResponse(status=204)
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
            return HttpResponse(status=204)
    else:
        form = MovieForm(instance=movie)
    return render(request, 'movie_form.html', {
        'form': form,
        'movie': movie,
    })
