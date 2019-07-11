from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    name = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.email

class Genre(models.Model):
    """Holds the Genres, like Action, Thriller"""
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Movie(models.Model):
    """ The Model to hold a list of Movies """
    name = models.CharField(max_length=250)
    genre = models.ForeignKey('Genre', related_name='movies', on_delete=models.CASCADE)
    stars = models.FloatField(default=1.0)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    """Stores Comments by users about the movie """
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    comment = models.TextField()
    visible = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
