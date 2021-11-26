import unittest
from src.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.waterloo = Song("Waterloo", "ABBA", "Europop")

    def test_song_has_name(self):
        self.assertEqual("Waterloo", self.waterloo.name)

    def test_song_has_artist(self):
        self.assertEqual("ABBA", self.waterloo.artist)

    def test_song_has_genre(self):
        self.assertEqual("Europop", self.waterloo.genre)