import unittest
import hashlib

from libs.commons import speed_test
from libs5.door_hacker import DoorHacker


class TestDoorHacker(unittest.TestCase):

    @speed_test
    def test_decode1(self):
        door_hacker = DoorHacker(
            algorithm=hashlib.md5, password_length=1, code='abc')
        result = door_hacker.decode()
        self.assertEqual(result, '1')

    @speed_test
    def test_decode2(self):
        door_hacker = DoorHacker(
            password_length=8, algorithm=hashlib.md5, code='abc')
        result = door_hacker.decode()
        self.assertEqual(result, '18f47a30')


if __name__ == '__main__':
    unittest.main()
