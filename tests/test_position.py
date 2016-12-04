import unittest

from libs.point import Point
from libs1.position import Position


class TestPosition(unittest.TestCase):

    def setUp(self):
        self.p = Position(0, 0, 'N')

    def test_turn_left(self):
        self.p.turn_left()
        self.assertEqual(self.p.orientation.position, 'W')

    def test_turn_right(self):
        self.p.turn_right()
        self.assertEqual(self.p.orientation.position, 'E')

    def test_move(self):
        self.p.move(10)
        res = Point(0, 10)
        self.assertEqual(self.p.point, res)


if __name__ == '__main__':
    unittest.main()
