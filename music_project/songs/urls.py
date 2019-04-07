from django.urls import path
from . import views
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

app_name = 'songs'

urlpatterns = [
    # /songs/
    path('songs/', views.IndexView.as_view(), name='index'),

    # /songs/71/
    path('songs/<int:pk>/', views.DetailView.as_view(), name='detail'),

    # /songs/album/add/
    path('songs/album/add/', views.AlbumCreate.as_view(), name='album-add'),

    # /songs/album/5/
    path('songs/<int:pk>/update/', views.AlbumUpdate.as_view(), name='album-update'),

    # /songs/album/5/delete/
    path('songs/<int:pk>/delete', views.AlbumDelete.as_view(), name='album-delete'),

    # /songs/
    path('songs/<int:id>/favorite_album', views.favorite_album, name='favorite_album'),

    # /songs/58/add_song/
    path('songs/<int:album_id>/add_song/', views.create_song, name='track-add'),

]
