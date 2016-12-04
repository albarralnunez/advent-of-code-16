from shape import Shape
import itertools


class Triangle(Shape):

    def __init__(self, c1, c2, h):
        self._c1 = c1
        self._c2 = c2
        self._h = h

    def __str__(self):
        return self._c1, self._c2, self._h

    @property
    def c1(self):
        return self._c1

    @c1.setter
    def c1(self, c1):
        self._c1 = c1

    @property
    def c2(self):
        return self._c2

    @c2.setter
    def c2(self, c2):
        self._c2 = c2

    @property
    def h(self):
        return self._h

    @h.setter
    def h(self, h):
        self._h = h

    def is_valid(self):
        c1c2, c1h, c2h = itertools.combinations(
            [self._c1, self._c2, self._h], 2)
        return (sum(c1c2) > self._h and
                sum(c1h) > self._c2 and
                sum(c2h) > self._c1)
