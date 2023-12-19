from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class Rating(models.Model):
    rating = models.FloatField()

    def __str__(self):
        return f'{self.rating}'


class Movie(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='movie_media')
    description = models.TextField()
    director = models.ForeignKey(Director, on_delete=models.PROTECT, related_name='movie')
    rating = models.OneToOneField(Rating, on_delete=models.CASCADE, related_name='movie')
    genre = models.ManyToManyField(Genre, related_name='movie')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
