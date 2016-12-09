import unittest

from libs.commons import speed_test
from libs8.screen import Screen


class TestPath(unittest.TestCase):

    @speed_test
    def test_rect(self):
        res = [[1, 1, 0, 0],
               [1, 1, 0, 0],
               [0, 0, 0, 0]]
        sc = Screen(4, 3)
        sc.rect(2, 2)
        self.assertEqual(sc.screen, res)

    @speed_test
    def test_rotate_row(self):
        res = [[1, 0, 0, 1],
               [1, 1, 0, 0],
               [0, 0, 0, 0]]
        sc = Screen(4, 3)
        sc.rect(2, 2)
        sc.rotate_row(0, 3)
        self.assertEqual(sc.screen, res)

    @speed_test
    def test_rotate_column(self):
        res = [[1, 1, 0, 0],
               [0, 1, 0, 0],
               [1, 0, 0, 0]]
        sc = Screen(4, 3)
        sc.rect(2, 2)
        sc.rotate_column(0, 2)
        self.assertEqual(sc.screen, res)

if __name__ == '__main__':
    unittest.main()
