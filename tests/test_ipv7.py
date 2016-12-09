import unittest

from libs.commons import speed_test
from libs7.ipv7 import IPv7


class TestIPv7(unittest.TestCase):

    @speed_test
    def test_has_tls1(self):
        ip = IPv7('abba[mnop]qrst')
        self.assertTrue(ip.has_tls())

    @speed_test
    def test_has_tls2(self):
        ip = IPv7('ioxxoj[asdfgh]zxcvbn')
        self.assertTrue(ip.has_tls())

    @speed_test
    def test_not_has_tls1(self):
        ip = IPv7('abcd[bddb]xyyx')
        self.assertFalse(ip.has_tls())

    @speed_test
    def test_not_has_tls2(self):
        ip = IPv7('aaaa[qwer]tyui')
        self.assertFalse(ip.has_tls())

    @speed_test
    def test_has_ssl1(self):
        ip = IPv7('aba[bab]xyz')
        self.assertTrue(ip.has_ssl())


    @speed_test
    def test_has_ssl2(self):
        ip = IPv7('aaa[kek]eke')
        self.assertTrue(ip.has_ssl())


    @speed_test
    def test_has_ssl3(self):
        ip = IPv7('zazbz[bzb]cdb')
        self.assertTrue(ip.has_ssl())

    @speed_test
    def test_has_ssl4(self):
        ip = IPv7('zabzba[azbz]cdb')
        self.assertTrue(ip.has_ssl())

    @speed_test
    def test_has_ssl5(self):
        ip = IPv7('zaza[azaz]azaz')
        self.assertTrue(ip.has_ssl())

    @speed_test
    def test_not_has_ssl1(self):
        ip = IPv7('xyx[xyx]xy')
        self.assertFalse(ip.has_ssl())

    @speed_test
    def test_not_has_ssl2(self):
        ip = IPv7('xya[xyx]xyx')
        self.assertFalse(ip.has_ssl())

    @speed_test
    def test_not_has_ssl3(self):
        ip = IPv7('xaya[atayaxyxae]axyxae')
        self.assertFalse(ip.has_ssl())

    @speed_test
    def test_not_has_ssl4(self):
        ip = IPv7('xa[aya]ax')
        self.assertFalse(ip.has_ssl())

    @speed_test
    def test_not_has_ssl5(self):
        ip = IPv7('c[d]abba[e]f')
        self.assertFalse(ip.has_ssl())

    @speed_test
    def test_not_has_ssl6(self):
        ip = IPv7('z[aza]azdz')
        self.assertFalse(ip.has_ssl())

    @speed_test
    def test_not_has_ssl7(self):
        ip = IPv7('z[aza]azdz[zaz]wer')
        self.assertFalse(ip.has_ssl())

if __name__ == '__main__':
    unittest.main()