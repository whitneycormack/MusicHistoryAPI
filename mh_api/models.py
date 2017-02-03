from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Artist(models.Model):
    artist_name = models.CharField(max_length=60)
    year_established = models.CharField(max_length=60)

    def __str__(self):
      return 'Artist Name: %s, Year Established: %s' % (self.artist_name, self.year_established)


class Genre(models.Model):
    genre_type = models.CharField(max_length=60)

    def __str__(self):
      return 'Genre: %s' % (self.genre_type)


class Album(models.Model):
    album_title = models.CharField(max_length=60)
    album_release_date = models.CharField(max_length=60)
    album_length = models.CharField(max_length=60)
    label = models.CharField(max_length=60)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
      return 'Album Title: %s, Album Release Date: %s, Album Length: %s, Label: %s, Artist Name: %s, Genre: %s' % (self.album_title, self.album_release_date, self.album_length, self.label, self.artist_name, self.genre_type)


class Song(models.Model):
    song_title = models.CharField(max_length=60)
    song_length = models.CharField(max_length=60)
    song_release_date = models.CharField(max_length=60)
    song_genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    song_artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
      return 'Song Title: %s, Song Length: %s, Song Release Date: %s, Genre: %s, Artist: %s, Album Title: %s' % (self.song_title, self.song_length, self.song_release_date, self.genre_type, self.artist_name, self.album_title)






