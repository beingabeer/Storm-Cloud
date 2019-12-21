from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from .formatChecker import ContentTypeRestrictedFileField


class Album(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=250)
    genre = models.CharField(max_length=100, blank=True)
    album_logo = models.ImageField(default='storm.png', upload_to='album_logo')
    date_created = models.DateTimeField(default=timezone.now)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.album_title + ' (by ' + self.artist + ')'

    def get_absolute_url(self):
        return reverse('songs:detail', kwargs={'pk': self.pk})


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250)
    # audio_file = models.FileField(upload_to='audio_files')
    audio_file = ContentTypeRestrictedFileField(upload_to='audio_files/', content_types=['audio/mp3', 'audio/mpeg', 'audio/mp3', ], max_upload_size=10485760)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title
