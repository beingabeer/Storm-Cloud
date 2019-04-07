from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class Album(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=250)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField(default='logo.jpg', upload_to='album_logo')
    date_created = models.DateTimeField(default=timezone.now)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.album_title + ' (by ' + self.artist + ')'

    def get_absolute_url(self):
        return reverse('songs:detail', kwargs={'pk': self.pk})


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250)
    audio_file = models.FileField(default='', upload_to='audio_files')
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title

    def get_absolute_url(self):
        return reverse('songs:detail', kwargs={'pk': self.pk})
