from django.urls import path
from . import views

app_name = 'songs'

urlpatterns = [
    # /songs/
    path('songs/', views.IndexView.as_view(), name='index'),

    # /songs/71/
    path('songs/<int:pk>/', views.DetailView.as_view(), name='detail'),
]
