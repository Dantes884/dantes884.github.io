from django.shortcuts import get_object_or_404
from django.views import generic

from apps.movie import models
from apps.movie_web import forms


class MovieView(generic.ListView):
    template_name = "movie_list.html"
    queryset = models.Movie.objects.all()


class MovieDetailView(generic.DetailView):
    template_name = "movie_detail.html"

    def get_object(self, **kwargs):
        movie_id = self.kwargs.get("id")
        return get_object_or_404(models.Movie, id=movie_id)


class MovieCreateView(generic.CreateView):
    template_name = "add_movie.html"
    form_class = forms.MovieForm
    success_url = "/movies/"
    queryset = models.Movie.objects.all()

    def form_valid(self, form):
        return super(MovieCreateView, self).form_valid(form=form)


class MovieUpdateView(generic.UpdateView):
    template_name = "movie_change.html"
    form_class = forms.MovieForm
    success_url = "/movies/"

    def get_object(self, **kwargs):
        movie_id = self.kwargs.get("id")
        return get_object_or_404(models.Movie, id=movie_id)

    def form_valid(self, form):
        return super(MovieUpdateView, self).form_valid(form=form)


class MovieDeleteView(generic.DeleteView):
    template_name = "delete_confirm.html"
    success_url = "/movies/"

    def get_object(self, **kwargs):
        movie_id = self.kwargs.get("id")
        return get_object_or_404(models.Movie, id=movie_id)
