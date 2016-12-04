import abc


class Encoder(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self, code, key):
        self.code = code
        self.key = key

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code):
        self._code = code

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, key):
        self._key = key

    @abc.abstractmethod
    def decode(self):
        pass


class DummyEncoder(Encoder):

    def decode(self):
        return self._code