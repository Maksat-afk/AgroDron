from django.http import JsonResponse
from django.views import View
from .models import Movie

class MovieListView(View):
    def get(self, request):
        movies = list(Movie.objects.values())
        return JsonResponse(movies, safe=False)

class MovieDetailView(View):
    def get(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        return JsonResponse({
            "title": movie.title,
            "description": movie.description,
            "producer": movie.producer,
            "duration": movie.duration
        })
