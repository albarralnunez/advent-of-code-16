import unittest

from libs4.caesar_cipher import CaesarCipher


class TestRoom(unittest.TestCase):

    def test_decrypt(self):
        cc = CaesarCipher('qzmt-zixmtkozy-ivhz', 343)
        result = cc.decode()
        self.assertTrue(result, 'very encrypted name')


if __name__ == '__main__':
    unittest.main()