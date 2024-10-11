from django.db import models
from tastypie.resources import ModelResource
from movies.models import Movie

# Create your models here.

class MovieResource(ModelResource):
  class Meta:
    queryset = Movie.objects.all()
    resource_name = 'movies'
    excludes = ['date_created']
    allowed_methods = ['get', 'post', 'put', 'delete']
    filtering = {
      'title': ['exact', 'startswith'],
      'release_year': ['exact'],
      'price': ['exact', 'lt', 'lte', 'gt', 'gte'],
      'genre': ['exact'],
      'number_in_stock': ['exact', 'lt', 'lte', 'gt', 'gte'],
      'daily_rate': ['exact', 'lt', 'lte', 'gt', 'gte'],
      'date_created': ['exact', 'lt', 'lte', 'gt', 'gte'],
    }
