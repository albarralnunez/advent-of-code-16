from libs.point import Point
from graph import Node


class Tail(Node):

    def __init__(self, tail_id, n=None, w=None, s=None, e=None):
        self.n = n
        self.w = w
        self.s = s
        self.e = e
        self.tail_id = tail_id

    @property
    def neighbors(self):
        return [x for x in [self.e, self.w, self.s, self.n] if x and
                isinstance(x, Corridor)]


class Corridor(Tail):

    def __init__(self, *args, **kwargs):
        super(Corridor, self).__init__(*args, **kwargs)
        self.bread_crumbs = False


class Wall(Tail):
    pass
