from django.shortcuts import render, get_object_or_404
from .models import Album
from django.http import Http404


def index(request):
    albums = Album.objects.all()
    context = {'albums': albums}
    return render(request, 'songs/index.html', context)


def detail(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist!")
    return render(request, "songs/detail.html", {'album': album})
