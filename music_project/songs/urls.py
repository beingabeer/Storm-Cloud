from django.urls import path
from . import views



urlpatterns = [
    # /songs/
    path('', views.index, name='index'),

    # /songs/71/
    path('<int:pk>/', views.detail, name='detail'),
]