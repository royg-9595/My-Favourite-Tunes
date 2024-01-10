from django.contrib import admin
from django.urls import path
from TuneTracker.views import SongList, SongDetail, SongCreate, ArtistCreate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', SongList.as_view(), name= 'songslist'),
    path('songview/<int:pk>/', SongDetail.as_view(), name= 'songview'),
    path('create_new', SongCreate.as_view(), name='songcreate'),
    path('add_artist', ArtistCreate.as_view(), name='artistcreate'),
]
