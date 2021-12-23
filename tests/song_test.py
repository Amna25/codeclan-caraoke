import unittest
from models.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song= Song("happy", "James Bay")

    def test_song_has_title(self):
        self.assertEqual("happy", self.song.title)

    def test_song_has_artist(self):
        self.assertEqual("James Bay", self.song.artist)