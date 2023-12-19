from django import forms
from apps.movie import models


class DirectorForm(forms.ModelForm):
    class Meta:
        model = models.Director
        fields = "__all__"


class RatingForm(forms.ModelForm):
    class Meta:
        model = models.Rating
        fields = "__all__"


class GenreForm(forms.ModelForm):
    class Meta:
        model = models.Genre
        fields = "__all__"


class MovieForm(forms.ModelForm):
    class Meta:
        model = models.Movie
        fields = "__all__"
