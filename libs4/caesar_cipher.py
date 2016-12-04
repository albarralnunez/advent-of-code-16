from encoder import Encoder


class CaesarCipher(Encoder):

    def __convert(self, letter):
        if letter == ' ':
            return ' '
        shifted = ord(letter) + self._key % 26
        if shifted > ord('z'):
            shifted = shifted - ord('z') + ord('a') - 1
        return chr(shifted)

    def decode(self):
        return ''.join(self.__convert(x) for x in self._code)
