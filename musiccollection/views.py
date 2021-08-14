from django.shortcuts import render, redirect, get_object_or_404
from .models import Album, Track
from .forms import AlbumForm


# Create your views here.
def list_albums(request):
    albums = Album.objects.all()
    return render(
        request,
        'musiccollection/list_albums.html',
        {'albums': albums}
        )


def add_album(request):
    if request.method == 'GET':
        form = AlbumForm()
    else: 
        form = AlbumForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_albums')

    return render(
        request, 
        'musiccollection/add_album.html',
        {'form': form}
        )


def view_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    tracks = album.track.all()
    return render(
        request,
        'musiccollection/view_album.html', 
        {'album': album, 'tracks': tracks}
    )