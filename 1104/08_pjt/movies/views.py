from django.shortcuts import render
from django.views.decorators.http import require_safe
from .models import Movie, Genre
import random
# Create your views here.
@require_safe
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'movies/index.html',context)


@require_safe
def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    genres = movie.genres.all()
    context = {
        'movie': movie,
        'genres': genres
    }
    return render(request,'movies/detail.html',context)

@require_safe
def recommended(request):
    # 무비 다 받아서
    # 평점 8.5 이상인거 골라내서 AJAX로 넘겨준다.
    movies = Movie.objects.all()
    good_movies = []
    for i in range(len(movies)):
        if movies[i].vote_average >= 8.5:
            good_movies.append(movies[i])
    random_good_movies = random.sample(good_movies, 10)
    context = {
        'random_good_movies': random_good_movies
    }
    return render(request, 'movies/recommended.html', context)