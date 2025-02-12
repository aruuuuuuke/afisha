from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    duration = models.PositiveIntegerField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movies')


    def __str__(self):
        return self.title

STARS = (
    (1, '⭐'),
    (2, '⭐⭐'),
    (3, '⭐⭐⭐'),
    (4, '⭐⭐⭐⭐'),
    (5, '⭐⭐⭐⭐⭐'),
)
class Review(models.Model):
    text = models.TextField()
    rating = models.IntegerField(default=5, choices=STARS, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')

