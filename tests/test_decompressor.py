import unittest
import os
from libs.commons import speed_test
from libs9.decompressor import Decompressor


class TestDecompressor(unittest.TestCase):

    @speed_test
    def test_decompressor_1(self):
        decompressor = Decompressor(file='A(1x5)BC')
        f = decompressor()
        self.assertEqual(f, 'ABBBBBC')

    @speed_test
    def test_decompressor_2(self):
        decompressor = Decompressor(file='(3x3)XYZ')
        f = decompressor()
        self.assertEqual(f, 'XYZXYZXYZ')

    @speed_test
    def test_decompressor_3(self):
        decompressor = Decompressor(file='A(2x2)BCD(2x2)EFG')
        f = decompressor()
        self.assertEqual(f, 'ABCBCDEFEFG')

    @speed_test
    def test_decompressor_4(self):
        decompressor = Decompressor(file='(6x1)(1x3)A')
        f = decompressor()
        self.assertEqual(f, '(1x3)A')

    @speed_test
    def test_decompressor_5(self):
        decompressor = Decompressor(file='ADVENT')
        f = decompressor()
        self.assertEqual(f, 'ADVENT')

if __name__ == '__main__':
    unittest.main()
