import unittest
from src.guest import Guest
from src.song import Song
from src.room import Room

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.waterloo = Song("Waterloo", "ABBA", "Europop")
        self.september = Song("September", "Earth, Wind & Fire", "R&B")
        self.seventies_playlist = [self.waterloo, self.september]
        self.room = Room("70's classics", self.seventies_playlist)

    def test_room_has_name(self):
        self.assertEqual("70's classics", self.room.name)

    def test_room_has_playlist(self):
        self.assertEqual(2, len(self.room.playlist))

    def test_room_has_guests(self):
        self.assertEqual(0, len(self.room.guests))

    def test_room_can_count_guests(self):
        self.assertEqual(0, self.room.count_guests())