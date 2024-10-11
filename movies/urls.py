from django.urls import path
from .views import index, detail

app_name = 'movies'

# movies/
urlpatterns = [
  path('', index, name='index'),
  path('<int:movie_id>', detail, name='detail'),
]  