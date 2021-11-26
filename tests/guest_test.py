import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.andrew = Guest("Andrew")

    def test_guest_has_name(self):
        self.assertEqual("Andrew", self.andrew.name)