import unittest

from libs.commons import speed_test
from libs.point import Point
from libs1.path import Path


class TestPath(unittest.TestCase):

    def setUp(self):
        self.p = Path()

    @speed_test
    def test_move(self):
        self.p.move('L3')
        self.assertEqual(
            self.p.position.orientation.position, 'W')
        self.assertEqual(self.p.position.point, Point(-3, 0))

if __name__ == '__main__':
    unittest.main()