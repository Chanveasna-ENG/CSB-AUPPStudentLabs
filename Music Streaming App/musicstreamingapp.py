# Prototype code, you can follow different implementation process

class Song:
    "I choose to use class to represent song, because it is more convenient to store song information in a class" 
    def __init__(self, title, artist, album, genre, length): 
        self.title = title
        self.artist = artist
        self.album = album
        self.genre = genre
        self.length = length


class MusicLibrary:
    """
    I choose to use dictionary to represent music library, because it does not allow duplicate keys/values and can access with key.
    """
    def __init__(self): 
        self.song_list = dict()

    def add_song(self, song): 
        self.song_list[f"{song.title} - {song.artist}"] = song
    
    def add_songs(self, songs):
        for song in songs:
            self.song_list[f"{song.title} - {song.artist}"] = song

    def get_songs_by_artist(self, artist): 
        return '\n'.join([f"{song.title} - {song.album}" for song in self.song_list.values() if song.artist == artist])

    def get_songs_by_album(self, album): 
        return '\n'.join([f"{song.title} - {song.artist}" for song in self.song_list.values() if song.album == album])

    def get_songs_by_genre(self, genre): 
        return '\n'.join([f"{song.title} - {song.artist}" for song in self.song_list.values() if song.genre == genre])

    def get_songs_by_title(self, title): 
        return '\n'.join([f"{song.album} - {song.artist}" for song in self.song_list.values() if song.title == title])


class Playlist:
    """
    I choose to use list to represent playlist, because it can be access with index so it is easy to maintain and reorder songs.
    """
    def __init__(self, name): 
        self.name = name
        self.song_list = list()
        self.song_set = set()

    def add_song(self, song): 
        if song not in self.song_set:
            self.song_list.append(song)
            self.song_set.add(song)
    
    def add_songs(self, songs): 
        for song in songs:
            if song not in self.song_set:
                self.song_list.append(song)
                self.song_set.add(song)

    def remove_song(self, song): 
        if song in self.song_set:
            self.song_list.remove(song)
            self.song_set.remove(song)

    def reorder_songs(self, song, index): 
        if song in self.song_set:
            self.song_list.remove(song)
            self.song_list.insert(index, song)

    def display_playlist(self): 
        for index, song in enumerate(self.song_list):
            print(f"{index+1}. {song.title} - {song.artist}")
