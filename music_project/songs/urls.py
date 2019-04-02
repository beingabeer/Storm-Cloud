from django.urls import path
from . import views



urlpatterns = [
    # /songs/
    path('songs/', views.index, name='index'),

    # /songs/71/
    path('songs/<int:album_id>/', views.detail, name='detail'),
]
