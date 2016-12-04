import unittest

from libs.commons import speed_test
from libs1.cardinal_points import CardinalPoints, InvalidOrientation


class TestCardinalPoints(unittest.TestCase):

    def setUp(self):
        self.cp = CardinalPoints()

    @speed_test
    def test_turn_left(self):
        self.cp.turn_left()
        self.assertEqual(self.cp.position, 'W')

    @speed_test
    def test_turn_right(self):
        self.cp.turn_right()
        self.assertEqual(self.cp.position, 'E')

    def test_invalid_orientation(self):
        with self.assertRaises(InvalidOrientation) as context:
            CardinalPoints(orientation='ERROR')
        message = "Orientation must be one " \
                  "of this options ['N', 'W', 'S', 'E']"
        self.assertTrue(message in context.exception)

if __name__ == '__main__':
    unittest.main()
