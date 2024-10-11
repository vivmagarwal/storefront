from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Movie
import logging
logger = logging.getLogger(__name__)


# Create your views here.

def index(request):
  # SELECT * FROM movies_movie
  movies = Movie.objects.all()

  # SELECT * FROM movies_movie WHERE id = 1
  # movie1 = Movie.objects.get(id=1)

  # SELECT * FROM movies_movie WHERE release_year = 2000
  # filteredMovies = Movie.objects.filter(release_year=2000) 

  # output = ', '.join([m.title for m in Movies])
  # return HttpResponse(output)
  
  return render(request, 'movies/index.html', {'movies': movies})

def detail(request, movie_id):
  # try:
    # return HttpResponse('Movie ID: ' + str(movie_id))
    # movie = Movie.objects.get(id=movie_id)
    # logger.info(movie.__dict__)
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})
  # except Movie.DoesNotExist:
  #   raise Http404('Movie not found')

