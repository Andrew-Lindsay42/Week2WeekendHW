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

    def test_room_can_add_guest(self):
        andrew = Guest("Andrew")
        self.room.add_guest(andrew)
        self.assertEqual(1, self.room.count_guests())

    def test_room_can_remove_guest_in_room(self):
        andrew = Guest("Andrew")
        emily = Guest("Emily")
        self.room.add_guest(andrew)
        self.room.add_guest(emily)

        self.room.remove_guest(andrew)
        self.assertEqual(1, self.room.count_guests())

    def test_room_can_remove_guest_not_in_room(self):
        andrew = Guest("Andrew")
        fred = Guest("Fred")
        self.room.add_guest(andrew)

        self.assertEqual("Guest not found", self.room.remove_guest(fred))