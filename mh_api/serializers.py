from django.contrib.auth.models import User, Group
from rest_framework import serializers
from mh_api.models import Album, Artist, Song, Genre

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
      model = User
      fields = (
        'url',
        'id',
        'username',
        'email',
        'groups'
      )

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
      model = Group
      fields = (
        'url',
        'id',
        'name'
      )

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
      model = Album
      fields = (
        'url',
        'id',
        'album_title',
        'album_release_date',
        'album_length',
        'label',
        'artist',
        'genre',
      )

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
      model = Artist
      fields = (
        'url',
        'id',
        'artist_name',
        'year_established',
      )


class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
      model = Song
      fields = (
        'url',
        'id',
        'song_title',
        'song_length',
        'song_release_date',
        'song_genre',
        'song_artist',
        'album',
      )


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
      model = Genre
      fields = (
        'url',
        'id',
        'genre_type',
      )












