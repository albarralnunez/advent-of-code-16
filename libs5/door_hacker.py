import hashlib
from multiprocessing import Pool
from libs4.encoder import Encoder


class DoorHacker(object):

    CHUNKS = 100000
    NUM_PROCESS = 4

    def __init__(self, algorithm, password_length, code):
        self._algorithm = algorithm
        self._password_length = password_length
        self._code = code
        self._index = 0

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value

    @property
    def password_length(self):
        return self._password_length

    @password_length.setter
    def password_length(self, value):
        self._password_length = value

    @property
    def algorithm(self):
        return self._algorithm

    @algorithm.setter
    def algorithm(self, value):
        self._algorithm = value

    def __generate_hash(self, index):
        combination = "%s%s" % (self.code, index)
        return hashlib.md5(combination).hexdigest()

    @staticmethod
    def __is_valid_hash(hashed):
        return hashed[:5] == '00000'

    def __get_character(self, start_index):
            index = start_index
            password = {}
            while index < self.CHUNKS:
                possible_hash = self.__generate_hash(index)
                if self.__is_valid_hash(possible_hash):
                    password[index] = possible_hash[5]
                index += 1
            return password

    def decode(self):
        pool = Pool(self.NUM_PROCESS)
        password = {}
        while len(password) < self._password_length:
            results = pool.map(
                self.__get_character,
                range(self._index, self.NUM_PROCESS*self.CHUNKS, self.CHUNKS))
            map(lambda x: password.update(x), results)
        self._index += self.NUM_PROCESS * self.CHUNKS
        return password.values()[:self._password_length]
