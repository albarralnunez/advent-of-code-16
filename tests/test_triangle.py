import unittest

from libs3.triangle import Triangle


class TestTriangle(unittest.TestCase):

    def test_invalid(self):
        t = Triangle(5, 10, 25)
        self.assertFalse(t.is_valid())

    def test_valid(self):
        t = Triangle(1, 1, 1)
        self.assertTrue(t.is_valid())


if __name__ == '__main__':
    unittest.main()