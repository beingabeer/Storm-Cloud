from django.shortcuts import render, get_object_or_404, redirect
from .models import Album, Song
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import JsonResponse
from .forms import SongForm
from django.contrib import messages


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


def favorite_album(request, id):
    album = get_object_or_404(Album, pk=id)
    try:
        if album.is_favorite:
            album.is_favorite = False
        else:
            album.is_favorite = True
        album.save()
    except (KeyError, Album.DoesNotExist):
        return JsonResponse({'success': False})
    else:
        return redirect('songs:index')


AUDIO_FILE_TYPES = ['wav', 'mp3', 'ogg']


def create_song(request, album_id):
    form = SongForm(request.POST or None, request.FILES or None)
    album = get_object_or_404(Album, pk=album_id)
    if form.is_valid():
        albums_songs = album.song_set.all()
        for s in albums_songs:
            if s.song_title == form.cleaned_data.get("song_title"):
                context = {
                    'album': album,
                    'form': form,
                    'error_message': 'You already added that song',
                }
                return render(request, 'songs/song_form.html', context)
        song = form.save(commit=False)
        song.album = album
        song.audio_file = request.FILES['audio_file']
        file_type = song.audio_file.url.split('.')[-1]
        file_type = file_type.lower()
        if file_type not in AUDIO_FILE_TYPES:
            context = {
                'album': album,
                'form': form,
                'error_message': 'Audio file must be WAV, MP3, or OGG',
            }
            return render(request, 'songs/song_form.html', context)

        song.save()
        return redirect('songs:detail', pk=album_id)
    context = {
        'album': album,
        'form': form,
    }
    return render(request, 'songs/song_form.html', context)


# def index(request):
#     albums = Album.objects.all()
#     context = {'albums': albums}
#     return render(request, 'songs/index.html', context)


# def detail(request, album_id):
#     album = get_object_or_404(Album, pk=album_id)
#     return render(request, "songs/detail.html", {'album': album})
