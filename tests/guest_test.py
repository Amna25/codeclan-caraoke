import unittest
from models.song import Song
from models.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.song_1= Song("happy", "James Bay")
        self.song_2 = Song("best day", "David Bowie")
        self.song_3= Song("Ace of spades", "Motherhead")
        self.songs = [self.song_1, self.song_2, self.song_3]

        song = Song("Ace of spades", "Motherhead")
        self.guest = Guest("Ruby", 50, song)

    def test_has_name(self):
        self.assertEqual("Ruby", self.guest.name)

    def test_has_wallet(self):
        self.assertEqual(50, self.guest.wallet)
    
    def test_has_favourite_song(self):
        self.assertEqual("Ace of spades", self.guest.favourite_song.title)

    def test_guest_has_enough_money(self):
        self.guest.has_enough_money()
        self.assertEqual(50, self.guest.wallet)
    
    def test_can_afford_20(self):
        self.assertEqual(True, self.guest.can_afford(10))

    def test_cannot_afford_60(self):
        self.assertEqual(False, self.guest.can_afford(60))

    def test_guest_can_pay(self):
        self.guest.can_pay(20)
        self.assertEqual(30, self.guest.wallet)

    def test_guest_can_cheer(self):
        result = self.guest.cheer(self.songs)
        self.assertEqual("Whoo Hoo!", result)

    def test_guest_cannot_cheer(self):
        song = Song("Highway to hell", "Mike")
        guest = Guest("Jim", 5, song)
        self.assertEqual(None, guest.cheer(self.songs))

