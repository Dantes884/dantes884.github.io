from django.urls import path
from . import views

app_name = 'movie_web'

urlpatterns = [
    path("", views.MovieView.as_view()),
    path("<int:id>/change/", views.MovieUpdateView.as_view()),
    path("<int:id>/delete/", views.MovieDeleteView.as_view()),
    path("<int:id>/", views.MovieDetailView.as_view()),
    path("add/", views.MovieCreateView.as_view(), name='add_movie'),
]
