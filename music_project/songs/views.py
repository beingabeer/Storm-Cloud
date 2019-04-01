from django.shortcuts import render
from django.http import HttpResponse
from .models import Album

# albums = [
#     {
#         'artist': 'Usher',
#         'album_title': 'Over the moon',
#         'genre': 'Hip-Hop'
#     },
#     {
#         'artist': 'Taylor Swift',
#         'album_title': 'Red',
#         'genre': 'Country'
#     }
# ]


def index(request):
    albums = Album.objects.all()
    context = {
        'albums': albums
    }
    return render(request, 'songs/index.html', context)



def detail(request, pk):
    return HttpResponse("<h2>Details for Album id: " + str(pk) +  "</h2>")
