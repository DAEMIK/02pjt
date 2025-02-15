from django.db import models
from movies.models import Movie

# Create your models here.

class Reviews(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    author = models.CharField(max_length = 255)
    content = models.TextField()
    rating = models.FloatField()

    def __str__(self):
        return self.movie