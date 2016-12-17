import unittest

from libs.commons import speed_test
from libs12.assembunny import Assembunny


class TestAssembunny(unittest.TestCase):

    @speed_test
    def test_turn_left(self):
        ops = ['cpy 41 a', 'inc a', 'inc a', 'dec a', 'jnz a 2', 'dec a']
        a = Assembunny(operations=ops)
        a.run()
        print a._reg

if __name__ == '__main__':
    unittest.main()
