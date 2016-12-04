import abc


class Shape(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def is_valid(self):
        pass
