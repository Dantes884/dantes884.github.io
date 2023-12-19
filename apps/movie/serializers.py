from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.movie.models import Director, Genre, Rating, Movie


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'id title description'.split()


class MovieDetailSerializer(serializers.ModelSerializer):
    director = DirectorSerializer()
    genre = GenreSerializer(many=True)
    rating = RatingSerializer()

    class Meta:
        model = Movie
        fields = '__all__'


class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=1000)
    director_id = serializers.IntegerField()
    rating_id = serializers.IntegerField()
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(),
        slug_field='id',
        many=True
    )

    def validate_director_id(self, director_id):
        try:
            Director.objects.get(id=director_id)
        except Director.DoesNotExist:
            raise ValidationError(f'Director with id ({director_id}) not found')
        return director_id

    def validate_rating_id(self, rating_id):
        try:
            Rating.objects.get(id=rating_id)
        except Rating.DoesNotExist:
            raise ValidationError(f'Director with id ({rating_id}) not found')
        return rating_id

    @staticmethod
    def validate_genre(value):
        if not value:
            raise serializers.ValidationError("Поле 'genre' не может быть пустым.")
        return value
