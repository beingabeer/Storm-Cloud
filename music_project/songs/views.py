from django.shortcuts import render, get_object_or_404
from .models import Album, Song
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import JsonResponse


class IndexView(ListView):
    model = Album
    template_name = 'songs/index.html'
    context_object_name = 'albums'
    ordering = ['-date_created']

    # def get_queryset(self):
    # return Album.objects.all()


class DetailView(DetailView):
    model = Album
    template_name = 'songs/detail.html'


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumDelete(DeleteView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']
    success_url = reverse_lazy('songs:index')


def favorite_album(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        if album.is_favorite:
            album.is_favorite = False
        else:
            album.is_favorite = True
        album.save()
    except (KeyError, Album.DoesNotExist):
        return JsonResponse({'success': False})
    else:
        return JsonResponse({'success': True})


# def index(request):
#     albums = Album.objects.all()
#     context = {'albums': albums}
#     return render(request, 'songs/index.html', context)


# def detail(request, album_id):
#     album = get_object_or_404(Album, pk=album_id)
#     return render(request, "songs/detail.html", {'album': album})
