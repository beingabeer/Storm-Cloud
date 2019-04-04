from django.urls import path
from . import views

app_name = 'songs'

urlpatterns = [
    # /songs/
    path('songs/', views.IndexView.as_view(), name='index'),

    # /songs/71/
    path('songs/<int:pk>/', views.DetailView.as_view(), name='detail'),

    # /songs/album/add/
    path('songs/album/add/', views.AlbumCreate.as_view(), name='album-add'),

    # /songs/album/5/
    path('songs/album/<int:pk>/', views.AlbumUpdate.as_view(), name='album-update'),

    # /songs/album/5/delete/
    path('songs/album/<int:pk>/delete', views.AlbumDelete.as_view(), name='album-delete'),
]
