class Song:
    """ Simple Song class with info"""

    def __init__(self, title, artist, duration=None):
        self._title = title
        self._artist = artist
        self._duration = duration
        print("Album created by ", title)


class Album:
    """ Simple songs album class

    Attributes:
        name(str): name of album
    """

    def __init__(self, name, year, artist=None):
        self._name = name
        self._year = year
        self._tracks = []
        if(artist is None):
            self._artist = Artist("Various Artist")
        else:
            self._artist = artist
        print("Album Name ", name)

    def add_song(self, song, position=None):
        if position is None:
            self._tracks.append(song)
        else:
            self._tracks.insert(position, song)


class Artist(object):
    def __init__(self, name, albums=[]):
        self._name = name
        self._albums = albums
        print("Artist Name ", name)

    def add_album(self, album):
        self._albums.append(album)


# No reference so GC
# Circular Object reference and GC problem
# Album (tracks List[Song]) --> Song (artist) --> Artist (albums List[Albums]) --> Album


def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open("albums.txt", "r") as albums:
        for line in albums:
            artist_field, album_field, year_filed, song_field = tuple(
                line.strip('\n').split('\t'))
            year_filed = int(year_filed)

            # print(artist_field, album_field, year_filed, song_field)
            if new_artist is None:
                new_artist = Artist(artist_field)
            elif new_artist._name != artist_field:
                new_artist.add_album(new_album)
                artist_list.append(new_artist)
                new_artist = Artist(artist_field)
                new_album = None

            if new_album is None:
                new_album = Album(album_field, year_filed, new_artist)
            elif new_album._name != artist_field:
                new_album.add_album(new_album)
                # artist_list.append(new_artist)
                new_album = Album(album_field, year_filed, new_artist)
                # new_album = None

            new_song = Song(song_field, new_artist)
            new_album.add_song(new_song)

            if new_artist is not None:
                if new_album is not None:
                    new_artist.add_album(new_album)
                artist_list.append(new_artist)

    return artist_list


if __name__ == '__main__':
    load_data()
