from django import forms
from .models import Album, Track


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = [
            'title',
            'artist',
            'release_year', 
            'album_art'
        ]