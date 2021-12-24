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

    def test_room_add_money_to_till(self):
        self.room.add_to_till(5)
        self.assertEqual(5, self.room.till)

    def test_can_check_in_guests(self):
        self.room.check_in_guests(self.guest_1)
        self.assertEqual(1, self.room.guests_count())

    def test_can_check_in_multiple_guests(self):
        self.room.check_in_guests(self.guest_1)
        self.room.check_in_guests(self.guest_2)
        self.assertEqual(2, self.room.guests_count())

    def test_can_check_out_guests(self):
        self.room.check_in_guests(self.guest_1)
        self.room.check_out_guests(self.guest_1)
        self.assertEqual(0, self.room.guests_count())

    def test_can_add_song(self):
        song = Song("Black Hill", "JJR")
        self.room.add_song(song)
        self.assertEqual(1, self.room.number_of_songs())

    def test_can_add_multiple_songs(self):
        self.room.add_song(self.song_1)
        self.room.add_song(self.song_2)
        self.assertEqual(2, self.room.number_of_songs())

    



        



        
