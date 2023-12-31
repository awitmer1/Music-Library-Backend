from django.db import models

# Create your models here.

class Song(models.Model):
    artist = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    album = models.CharField(max_length=255)
    release_date = models.DateField()
    genre = models.CharField(max_length=255)