from django import forms
from .models import torrent

class TorrentForm(forms.ModelForm):
    class Meta:
        model = torrent
        fields = ['title', 'description', 'image', 'language', 'date', 'torrent_file']
