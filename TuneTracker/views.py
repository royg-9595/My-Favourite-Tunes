from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Song, Artist
from django.urls import reverse_lazy

class SongList(ListView):
    model = Song
    context_object_name = 'Songs'
    template_name = 'list.html'

class SongDetail(DetailView):
    model=Song
    context_object_name = 'song'
    template_name = 'song.html'
    
class SongCreate(CreateView):
    model = Song
    template_name = 'songform.html'
    fields = ['title', 'artist']
    success_url = reverse_lazy('songslist')

    def form_valid(self, form):
        return super().form_valid(form)  

class ArtistCreate(CreateView):
    model = Artist
    template_name = 'artistform.html'
    fields = ['name']
    success_url = reverse_lazy('songcreate')

    def form_valid(self, form):
        return super().form_valid(form)
# Create your views here.
