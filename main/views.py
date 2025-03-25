from django.shortcuts import render, get_object_or_404
from .models import Song

def index(request):
    songs = Song.objects.all()
    play_song_id = request.GET.get('play',None)
    play_song = None
    
    if play_song_id:
        play_song = get_object_or_404(Song, id=play_song_id)
    
    return render(request,'main/index.html',{'songs':songs, 'play_song': play_song})