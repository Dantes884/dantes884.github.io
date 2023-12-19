from rest_framework import generics
from rest_framework.permissions import AllowAny

from apps.movie.models import Director, Genre, Rating, Movie
from apps.movie.serializers import DirectorSerializer, GenreSerializer, RatingSerializer, MovieSerializer, \
    MovieValidateSerializer, MovieDetailSerializer
from apps.movie.utils import TestPagination


class DirectorListView(generics.ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    pagination_class = TestPagination
    permission_classes = [AllowAny]


class GenreListView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    pagination_class = TestPagination
    permission_classes = [AllowAny]


class RatingListView(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    pagination_class = TestPagination
    permission_classes = [AllowAny]


class MovieListView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    permission_classes = [AllowAny]
    pagination_class = TestPagination

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieSerializer
        elif self.request.method == 'POST':
            return MovieValidateSerializer


class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieDetailSerializer
        elif self.request.method == 'PUT':
            return MovieValidateSerializer
        elif self.request.method == 'PATCH':
            return MovieValidateSerializer
