import unittest
from src.guest import Guest
from src.song import Song
from src.room import Room

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.waterloo = Song("Waterloo", "ABBA", "Europop")
        self.september = Song("September", "Earth, Wind & Fire", "R&B")
        self.seventies_playlist = [self.waterloo, self.september]
        self.room = Room("70's classics", self.seventies_playlist, 5, 5.0)

    def test_room_has_name(self):
        self.assertEqual("70's classics", self.room.name)

    def test_room_has_playlist(self):
        self.assertEqual(2, len(self.room.playlist))

    def test_room_has_guests(self):
        self.assertEqual(0, len(self.room.guests))

    def test_room_has_capacity(self):
        self.assertEqual(5, self.room.capacity)

    def test_room_has_fee(self):
        self.assertEqual(5.0, self.room.fee)

    def test_room_has_takings(self):
        self.assertEqual(0, self.room.takings)

    def test_room_can_check_takings(self):
        room = Room("", [], 5, 5.0)
        room.takings = 10.0
        self.assertEqual(10.0, room.check_takings())

    def test_room_can_add_takings(self):
        self.room.add_takings(20)
        self.assertEqual(20, self.room.check_takings())

    def test_room_can_count_guests(self):
        self.assertEqual(0, self.room.count_guests())

    def test_room_can_add_guest_space(self):
        andrew = Guest("Andrew", 20.00, self.waterloo)
        self.room.add_guest(andrew)

        self.assertEqual(1, self.room.count_guests())
        self.assertEqual(15, andrew.wallet)
        self.assertEqual(5, self.room.check_takings())

    def test_room_can_add_guest_no_space(self):
        tiny_room = Room("Cupboard", [], 0, 0)
        andrew = Guest("Andrew", 20.00, self.waterloo)

        self.assertEqual("Sorry, room's all full!", tiny_room.add_guest(andrew))
        self.assertEqual(0, tiny_room.count_guests())
        self.assertEqual(20, andrew.wallet)
        self.assertEqual(0, tiny_room.check_takings())

    def test_room_has_remaining_capacity(self):
        andrew = Guest("Andrew", 20.00, self.waterloo)
        emily = Guest("Emily", 10.00, self.waterloo)
        self.room.add_guest(andrew)
        self.room.add_guest(emily)

        self.assertEqual(3, self.room.remaining_capacity())

    def test_room_can_remove_guest_in_room(self):
        andrew = Guest("Andrew", 20.00, self.waterloo)
        emily = Guest("Emily", 10.00, self.waterloo)
        self.room.add_guest(andrew)
        self.room.add_guest(emily)

        self.room.remove_guest(andrew)
        self.assertEqual(1, self.room.count_guests())

    def test_room_can_remove_guest_not_in_room(self):
        andrew = Guest("Andrew", 20.00, self.waterloo)
        fred = Guest("Fred", 10.00, self.waterloo)
        self.room.add_guest(andrew)

        self.assertEqual("Guest not found", self.room.remove_guest(fred))

    def test_room_can_count_songs(self):
        self.assertEqual(2, self.room.count_songs())

    def test_room_can_add_song(self):
        one_that_I_want = Song("You're the one that I want", "Grease", "Pop")

        self.room.add_song(one_that_I_want)
        self.assertEqual(3, self.room.count_songs())

    def test_room_can_remove_song_in_playlist(self):
        self.room.remove_song(self.waterloo)
        self.assertEqual(1, self.room.count_songs())

    def test_room_can_remove_song_not_in_playlist(self):
        one_that_I_want = Song("You're the one that I want", "Grease", "Pop")
        self.assertEqual("Song not in playlist", self.room.remove_song(one_that_I_want))

    def test_room_has_favourite_guest_cheers(self):
        andrew = Guest("Andrew", 20.00, self.waterloo)
        self.assertEqual("Whoooo!", self.room.add_guest(andrew))

    def test_room_cannot_add_poor_guest(self):
        pauper = Guest("Steve", 0, self.waterloo)
        self.assertEqual("Sorry, you don't have enough money.", self.room.add_guest(pauper))

    def test_room_can_add_guests_space(self):
        andrew = Guest("Andrew", 20.00, self.waterloo)
        emily = Guest("Emily", 10.00, self.waterloo)
        group = [andrew, emily]

        self.room.add_multiple_guests(group)

        self.assertEqual(2, self.room.count_guests())
        self.assertEqual(3, self.room.remaining_capacity())

    def test_room_can_add_guests_no_space(self):
        andrew = Guest("Andrew", 20.00, self.waterloo)
        emily = Guest("Emily", 10.00, self.waterloo)
        group = [andrew, emily]
        small_room = Room("Sound booth", [], 1, 0)

        self.assertEqual("Sorry guys, we can't fit you all in", small_room.add_multiple_guests(group))