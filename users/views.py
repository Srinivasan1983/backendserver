from rest_framework import generics
from .models import Genre, Movie, Comment

from . import models
from .serializers import UserSerializer, GenreSerializer, MovieSerializer, CommentSerializer

class UserListView(generics.ListCreateAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = UserSerializer

class GenreListCreate(generics.ListCreateAPIView):
    """ List and create genres """
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    name = 'genre-list'
    #permission_classes = (permissions.IsAuthenticated, )


class GenreRetrieveUpdate(generics.RetrieveUpdateAPIView):
    """ Retrieve and update Genre information """
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    name = 'genre-detail'
    #permission_classes = (permissions.IsAuthenticated, )


class MovieListCreate(generics.ListCreateAPIView):
    """List and create movies """
    queryset = Movie.objects.all().order_by('name')
    serializer_class = MovieSerializer
    name = 'movie-list'
    #permission_classes = (permissions.IsAuthenticated, )


class MovieRetrieveUpdate(generics.RetrieveUpdateAPIView):
    """Retrieve and update a movie"""
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    name = 'movie-detail'
    #permission_classes = (permissions.IsAuthenticated, )


class CommentListCreate(generics.ListCreateAPIView):
    """ List or create a movie """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    #permission_classes = (permissions.IsAuthenticated, )


class CommentRetrieveUpdate(generics.RetrieveUpdateAPIView):
    """ List or create a movie """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    #permission_classes = (permissions.IsAuthenticated, )