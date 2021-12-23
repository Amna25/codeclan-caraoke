class Song:
    def __init__(self, tiltle, artist):
        self.title= tiltle
        self.artist = artist

    def equals(self, song):
        return song.title == self.title and song.artist == self.artist