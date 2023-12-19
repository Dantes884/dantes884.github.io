from django.urls import path

from apps.movie.views import *

urlpatterns = [
    path('director/', DirectorListView.as_view()),
    path('genre/', GenreListView.as_view()),
    path('rating/', RatingListView.as_view()),
    path('movie/', MovieListView.as_view()),
    path('movie/<int:pk>/', MovieDetailView.as_view()),
]
