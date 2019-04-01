from django.urls import path
from . import views



urlpatterns = [
    # /songs/
    path('songs/', views.index, name='index'),

    # /songs/71/
    path('songs/<int:pk>/', views.detail, name='detail'),
]