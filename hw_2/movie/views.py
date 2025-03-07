from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Movie

def movie_list(request):
    movies = list(Movie.objects.values())
    return JsonResponse(movies, safe=False)

def movie_detail(request, id):
    movie = get_object_or_404(Movie, id=id)
    return JsonResponse({"title": movie.title, "description": movie.description, "producer": movie.producer, "duration": movie.duration})

from django.shortcuts import render

