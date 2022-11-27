from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Genre, Movie
# Create your models here.

class User(AbstractUser):
    like_genres = models.ManyToManyField(Genre)
    like_movies = models.ManyToManyField(Movie, related_name="users")
    followings = models.ManyToManyField('self', symmetrical=False, related_name="followers")
    
    score = models.IntegerField(null=True, default=0)
    def __str__(self) :
        return self.username