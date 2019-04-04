from django.shortcuts import render, get_object_or_404
from .models import Album, Song
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class IndexView(ListView):
    template_name = 'songs/index.html'
    context_object_name = 'albums'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(DetailView):
    model = Album
    template_name = 'songs/detail.html'


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


# def index(request):
#     albums = Album.objects.all()
#     context = {'albums': albums}
#     return render(request, 'songs/index.html', context)


# def detail(request, album_id):
#     album = get_object_or_404(Album, pk=album_id)
#     return render(request, "songs/detail.html", {'album': album})
