from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=255)


class Movie(models.Model):
    release_date = models.DateTimeField(auto_now = True)
    popularity = models.FloatField()
    budget = models.IntegerField()
    revenue = models.IntegerField()
    runtime = models.IntegerField()
    title = models.CharField(max_length=255)
    genres = models.ManyToManyField(Genre, related_name= 'movies')



class Cast(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    name = models.CharField(max_length = 255)
    character = models.CharField(max_length = 255)
    order = models.IntegerField()