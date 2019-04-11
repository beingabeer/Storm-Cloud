from django.urls import path
from . import views
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.conf.urls import url

app_name = 'songs'

urlpatterns = [
    # /
    path('', views.IndexView.as_view(), name='index'),


    path('music/tracks/', views.songs, name='all-songs'),

    # /songs/71/
    path('music/<int:pk>/', views.DetailView.as_view(), name='detail'),

    # /music/album/add/
    path('music/album/add/', views.AlbumCreate.as_view(), name='album-add'),

    # /music/album/5/
    path('music/<int:pk>/update/', views.AlbumUpdate.as_view(), name='album-update'),

    # /music/album/5/delete/
    path('music/<int:pk>/delete/', views.AlbumDelete.as_view(), name='album-delete'),

    # /music/
    path('music/<int:id>/favorite_album', views.favorite_album, name='favorite_album'),

    # /music/58/add_song/
    path('music/<int:album_id>/add_song/', views.create_song, name='track-add'),


    path('music/<int:album_id>/delete_song/<int:song_id>/', views.delete_song, name='song-delete'),

    # url(r'^(?P<song_id>[0-9]+)/favorite/$', views.favorite_song, name='favorite_song'),
    path('music/<int:album_id>/favorite_song/<int:song_id>/', views.favorite_song, name='favorite_song'),
]
