import unittest
from libs import commons
import day6


class TestDay6(unittest.TestCase):

    @commons.speed_test
    def test_problem_1(self):
        messages = day6.get_messages('inputs/test_day_6.in')
        self.assertEqual(day6.problem_1(messages), 'easter')

    @commons.speed_test
    def test_problem_2(self):
        messages = day6.get_messages('inputs/test_day_6.in')
        self.assertEqual(day6.problem_2(messages), 'advent')


if __name__ == '__main__':
    unittest.main()
