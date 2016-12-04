import unittest

from libs.commons import speed_test
from libs.point import Point


class TestPoint(unittest.TestCase):

    def setUp(self):
        self.p = Point(0, 0)

    @speed_test
    def test_move(self):
        self.p.move(1, 2)
        self.assertEqual(self.p.x, 1)
        self.assertEqual(self.p.y, 2)

    @speed_test
    def test_tc_distance(self):
        new_p = Point(3, 5)
        tc_d = self.p.tc_distance(new_p)
        self.assertEqual(tc_d, -8)


if __name__ == '__main__':
    unittest.main()
