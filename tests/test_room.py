import unittest

from libs4.room import Room


class TestRoom(unittest.TestCase):

    def test_valid(self):
        room = Room('aaaaa bbb z y x', 123, 'abxyz')
        self.assertTrue(room.validate())

    def test_valid1(self):
        room = Room('a b c d e f g h', 987, 'abcde')
        self.assertTrue(room.validate())

    def test_valid2(self):
        room = Room('not a real room', 404, 'oarel')
        self.assertTrue(room.validate())

    def test_not_valid(self):
        room = Room('totally real room', 200, 'decoy')
        self.assertFalse(room.validate())


if __name__ == '__main__':
    unittest.main()