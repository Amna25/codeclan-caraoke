import unittest

from models.song import Song
from models.guest import Guest
from models.room import Room

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.song_1= Song("happy", "James Bay")
        self.song_2 = Song("best day", "David Bowie")
        self.song_3= Song("Ace of spades", "Motherhead")
        self.songs = [self.song_1, self.song_2, self.song_3]

        self.guest_1 = Guest("Jack", 20, self.song_1)
        self.guest_2 = Guest("Jill", 15,self.song_2)
        self.guest_3 = Guest("Victor", 50, self.song_3)
        self.guests = [self.guest_1, self.guest_2, self.guest_3]

        self.room = Room("Ball Room", 5, 10)

    def test_room_has_name(self):
        self.assertEqual("Ball Room", self.room.name)

    def test_room_guests_start_off_empty(self):
        self.assertEqual([], self.room.guests)

    def test_songs_start_off_empty(self):
        self.assertEqual([], self.room.songs)

    def test_room_has_capacity(self):
        self.assertEqual(5, self.room.capacity)

    def test_room_till_start_empty(self):
        self.assertEqual(0, self.room.till)
    
    def test_room_has_entry_fee(self):
        self.assertEqual(10, self.room.fee)
        
