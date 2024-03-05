class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.add_song_to_count(artist, genre)
        self.add_to_genres_count(genre)
        self.add_to_artist_count(artist)
        self.name = name
        self.artist = artist
        self.genre = genre

    @classmethod
    def add_song_to_count(cls, artist, genre, increment=1):
        cls.count += increment
        cls.artists.append(artist)
        cls.genres.append(genre)

    @classmethod
    def add_to_genres_count(cls, genre):
        cls.genre_count[genre] = cls.genres.count(genre)

    @classmethod
    def add_to_artist_count(cls, artist):
        cls.artist_count[artist] = cls.artists.count(artist)
