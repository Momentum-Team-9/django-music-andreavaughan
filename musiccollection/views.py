from django.shortcuts import render, redirect, get_object_or_404
from .models import Album, Track
# from .forms import AlbumForm


# Create your views here.
def list_albums(request):
    albums = Album.objects.all()
    return render(
        request,
        'musiccollection/list_albums.html',
        {'albums': albums}
        )