import unittest
from src.guest import Guest
from src.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.back_in_black = Song("Back in Black", "AC/DC", "Rock")
        self.andrew = Guest("Andrew", 20.00, self.back_in_black)

    def test_guest_has_name(self):
        self.assertEqual("Andrew", self.andrew.name)

    def test_guest_has_wallet(self):
        self.assertEqual(20.00, self.andrew.wallet)

    def test_guest_can_pay(self):
        self.andrew.pay_entry()
        self.assertEqual(15.00, self.andrew.wallet)

    def test_guest_has_favourite_song(self):
        self.assertEqual("Back in Black", self.andrew.favourite_song.name)