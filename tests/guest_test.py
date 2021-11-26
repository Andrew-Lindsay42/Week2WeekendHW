import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.andrew = Guest("Andrew", 20.00)

    def test_guest_has_name(self):
        self.assertEqual("Andrew", self.andrew.name)

    def test_guest_has_wallet(self):
        self.assertEqual(20.00, self.andrew.wallet)