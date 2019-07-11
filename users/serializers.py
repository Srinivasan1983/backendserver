from rest_framework import serializers
from . import models
from .models import Genre, Movie, Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('email', 'username', )

class GenreSerializer(serializers.HyperlinkedModelSerializer):
    """ A serializer for the Genre model """
    movies = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='movie-detail'
    )

    class Meta:
        model = Genre
        fields = ('url', 'id', 'name', 'description', 'movies')


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(), slug_field='name')
    
    """ A serializer for the Movie Model """
    class Meta:
        model = Movie
        fields = ('url','id', 'name', 'genre', 'stars', 'description', 'created')


class CommentSerializer(serializers.ModelSerializer):
    movie = serializers.SlugRelatedField(
        queryset=Movie.objects.all(), slug_field='name')
    """ Serializer for the Comment model """
    class Meta:
        model = Comment
        fields = ('id', 'user', 'movie', 'comment', 'visible', 'created')