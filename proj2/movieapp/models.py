from django.db import models

class MoviePreferences(models.Model):
    title = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    genre = models.CharField(max_length=255)
    min_avg_rating = models.FloatField()

    def __str__(self):
        return self.title