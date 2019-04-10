from django.shortcuts import render, get_object_or_404, redirect
from .models import Album, Song
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import JsonResponse
from .forms import SongForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required


class IndexView(LoginRequiredMixin, ListView):
    model = Album
    template_name = 'songs/index.html'
    context_object_name = 'albums'
    ordering = ['-date_created']


class DetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Album
    template_name = 'songs/detail.html'

    def test_func(self):
        album = self.get_object()
        if self.request.user == album.user:
            return True
        return False


class AlbumCreate(LoginRequiredMixin, CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AlbumUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Album
    template_name = 'songs/album_form_update.html'
    fields = ['artist', 'album_title', 'genre', 'album_logo']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        album = self.get_object()
        if self.request.user == album.user:
            return True
        return False


class AlbumDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Album
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        album = self.get_object()
        if self.request.user == album.user:
            return True
        return False


@login_required
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
                    'error_message': messages.warning(request, f'Song Already Exists!'),
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
                'error_message': messages.warning(request, f'Audio file must be WAV, MP3, or OGG'),
            }
            return render(request, 'songs/song_form.html', context)

        song.save()
        messages.success(request, f'Song Added!')
        return render(request, 'songs/detail.html', {'album': album})
    context = {
        'album': album,
        'form': form,
    }
    return render(request, 'songs/song_form.html', context)


def delete_song(request, album_id, song_id):
    album = get_object_or_404(Album, pk=album_id)
    song = Song.objects.get(pk=song_id)
    song.delete()
    return render(request, 'songs/detail.html', {'album': album})


def favorite_song(request, album_id, song_id):
    album = get_object_or_404(Album, pk=album_id)
    song = get_object_or_404(Song, pk=song_id)
    try:
        if song.is_favorite:
            song.is_favorite = False
        else:
            song.is_favorite = True
        song.save()
    except (KeyError, Song.DoesNotExist):
        return JsonResponse({'success': False})
    else:
        # return JsonResponse({'success': True})
        return render(request, 'songs/detail.html', {'album': album})


@login_required
def songs(request):
    # if not request.user.is_authenticated():
        # return render(request, 'music/login.html')
    # else:
    try:
        song_ids = []
        for album in Album.objects.all():
            for song in album.song_set.all():
                song_ids.append(song.pk)
        songs = Song.objects.all()
    except Album.DoesNotExist:
        songs = []
    return render(request, 'songs/tracks.html', {'song_list': songs})
