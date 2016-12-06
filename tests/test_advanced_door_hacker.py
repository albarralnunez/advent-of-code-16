import unittest
import hashlib

from libs.commons import speed_test
from libs5.advanced_door_hacker import AdvancedDoorHacker


class TestDoorHacker(unittest.TestCase):

    @speed_test
    def test_decode1(self):
        door_hacker = AdvancedDoorHacker(
            algorithm=hashlib.md5, password_length=1, code='abc')
        door_hacker.decode()
        self.assertEqual(door_hacker.password, '5')

    @speed_test
    def test_decode2(self):
        door_hacker = AdvancedDoorHacker(
            password_length=8, algorithm=hashlib.md5, code='abc')
        door_hacker.decode()
        self.assertEqual(door_hacker.password, '05ace8e3')


if __name__ == '__main__':
    unittest.main()
