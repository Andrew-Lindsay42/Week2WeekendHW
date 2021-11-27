import unittest
from src.guest import Guest
from src.song import Song
from src.room import Room

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.back_in_black = Song("Back in Black", "AC/DC", "Rock")
        self.andrew = Guest("Andrew", 20.00, self.back_in_black)

    def test_guest_has_name(self):
        self.assertEqual("Andrew", self.andrew.name)

    def test_guest_has_wallet(self):
        self.assertEqual(20.00, self.andrew.wallet)

    def test_guest_can_pay(self):
        self.andrew.pay_fee(5)
        self.assertEqual(15.00, self.andrew.wallet)

    def test_guest_has_favourite_song(self):
        self.assertEqual("Back in Black", self.andrew.favourite_song.name)

    def test_guest_fav_on_playlist(self):
        room = Room("Rock", [self.back_in_black], 5, 5)
        self.assertEqual("Whoooo!", self.andrew.check_favourite(room))

    def test_guest_fav_not_on_playlist(self):
        room = Room("Rock", [], 5, 5)
        self.assertEqual(None, self.andrew.check_favourite(room))

    def test_guest_can_afford(self):
        self.assertEqual(True, self.andrew.can_afford(5))

    def test_guest_cannot_afford(self):
        self.assertEqual(False, self.andrew.can_afford(20.01))