from django.contrib import admin
from .models import Movie
from .models import Genre

class GenreAdmin(admin.ModelAdmin):
  list_display = ('id', 'name')

class ModelAdmin(admin.ModelAdmin):
  exclude = ('date_created',) 
  list_display = ('title', 'release_year', 'price', 'genre', 'number_in_stock', 'daily_rate', 'date_created')

# Register your models here.
admin.site.register(Movie, ModelAdmin)
admin.site.register(Genre, GenreAdmin)

