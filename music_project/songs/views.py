from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>This will be a list of all Albums</h1>")


def detail(request, pk):
    return HttpResponse("<h2>Details for Album id: " + str(pk) +  "</h2>")