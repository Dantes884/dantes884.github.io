from django.contrib import admin

from apps.movie.models import Rating, Director, Genre, Movie

admin.site.register(Rating)
admin.site.register(Director)
admin.site.register(Genre)
admin.site.register(Movie)
