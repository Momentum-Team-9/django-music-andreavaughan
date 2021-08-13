from django.db import models
from django.db.models.fields import DateTimeField


# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255, null=True, blank=True)
    release_year = models.IntegerField()
    album_art = models.CharField(max_length=255, null=True, blank=True)
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}, {self.artist}, {self.release_year}'


class Track(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='track')
    name = models.CharField(max_length=255)
    featured_artist = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.name}, {self.featured_artist}'

