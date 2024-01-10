from django import forms
from .models import Song

class ModelForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'artist']
class ModelForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name']
