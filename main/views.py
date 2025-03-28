from django.shortcuts import render, get_object_or_404, redirect
from .models import Song
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def index(request):
    songs = Song.objects.all()
    play_song_id = request.GET.get('play',None)
    play_song = None
    
    if play_song_id:
        play_song = get_object_or_404(Song, id=play_song_id)
    
    return render(request,'main/index.html', {'songs':songs, 'play_song': play_song})

def register_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password != password2:
            print("Password didn't match!")
            return redirect('register_user')
        
        if User.objects.filter(username=username).exists():
            print("Username already taken!")
            return redirect('register_user')
        
        try:
            user = User.objects.create(username=username,password=password)
            user.save()
            login(request, user)
            print("Successfully registered!")
            return redirect('index')
        except Exception as e:
            print(f"Error: {e}")
            return redirect('register_user')
        
        
    return render(request,'main/register_user.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("Successfully logged in!!!")
            return redirect('index')
        else:
            print("Wrong credentions")
            return redirect('login_user')

    return render(request, 'main/login_user.html')

def logout_user(request):
    logout(request)
    print("Successfully logged out!!!")
    return redirect('index')

def create_playlist(request):
    if request.method == "POST":
        name_playlist = request.POST.get("name-playlist")

        if request.user.is_authenticated:
            create_playlist = Playlist.objects.create(name=name_playlist, user=request.user)
            create_playlist.save()
            return redirect("index")

        else:
            return redirect('index')
        
    return render(request, 'main/create_playlist.html')


def view_playlist(request, pk):
    if request.user.is_authenticated:
        playlist = Playlist.objects.get(id=pk, user=request.user)
        play_song_id = request.GET.get('play', None)
        shuffle = request.GET.get('shuffle', 'false') == 'true'
        play_song = None
        next_song = None

        playlist_list = list(playlist.song.all())
        
        if play_song_id:
            play_song = Song.objects.get(id=play_song_id)
        
        if shuffle and playlist_list:
            possible_songs = []

            for song in playlist_list:
                if song != play_song:
                    possible_songs.append(song)

            if possible_songs:
                next_song = choice(possible_songs)

        else:
            if play_song in playlist_list:
                current_index = playlist_list.index(play_song)
                loop_playlist = (current_index + 1) % len(playlist_list)
                next_song = playlist_list[loop_playlist]

        return render(request, 'main/view_playlist.html', {"playlist": playlist, "next_song": next_song, "play_song": play_song, "shuffle": shuffle})
    
    else:
        return redirect('index')

def all_playlists(request):
    if request.user.is_authenticated:
        playlists = Playlist.objects.filter(user=request.user)
        return render(request, 'main/all_playlists.html', {"playlists": playlists})

    else:
        return redirect('index')