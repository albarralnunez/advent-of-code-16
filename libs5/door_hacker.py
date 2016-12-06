from libs5.exceptions import TooMuchIterations


class DoorHacker(object):

    def __init__(self, algorithm, password_length, code, index=0,
                 index_out=None):
        self._algorithm = algorithm
        self._password_length = password_length
        self._code = code
        self._index_out = index_out
        self._index = index
        self._password = ''
        self._decoded = False

    @property
    def password(self):
        if not self._decoded:
            raise ValueError('You should run decode before')
        return self._password

    @property
    def index_out(self):
        return self._index_out

    @index_out.setter
    def index_out(self, value):
        self._index_out = value

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

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, value):
        self._index = value

    def _generate_hash(self, index):
        combination = "%s%s" % (self.code, index)
        return self._algorithm(combination).hexdigest()

    @staticmethod
    def _is_valid_hash(hashed):
        return hashed[:5] == '00000'

    def decode(self):
        while len(self._password) < self._password_length:
            possible_hash = self._generate_hash(self._index)
            if self._is_valid_hash(possible_hash):
                self._password += possible_hash[5]
            self._index += 1
            if self._index_out and self._index > self._index_out:
                raise TooMuchIterations('Too much iterations')
        self._decoded = True
