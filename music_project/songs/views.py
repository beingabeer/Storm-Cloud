from django.shortcuts import render, get_object_or_404
from .models import Album

def index(request):
    albums = Album.objects.all()
    context = {'albums': albums}
    return render(request, 'songs/index.html', context)


def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, "songs/detail.html", {'album': album})
