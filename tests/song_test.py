import unittest
from models.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song= Song("happy", "James Bay")

    def test_song_has_title(self):
        self.assertEqual("happy", self.song.title)

    def test_song_has_artist(self):
        self.assertEqual("James Bay", self.song.artist)

    def test_equals_return_true(self):
        song = Song("happy", "James Bay")
        result = self.song.equals(song)
        self.assertEqual(True, result)

    def test_equals_song_different_return_False(self):
        song = Song("Ace of Spades", "Iron Maiden")
        result = self.song.equals(song)
        self.assertEqual(False, result)
