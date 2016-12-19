from libs.graph.graph import Node


class Tail(Node):

    def __init__(self, tail_id, u=None, l=None, d=None, r=None):
        self.u = u
        self.l = l
        self.d = d
        self.r = r
        self.tail_id = tail_id

    @property
    def neighbors(self):
        return [x for x in [self.u, self.l, self.d, self.r] if x]

    @property
    def node_id(self):
        return self.tail_id


class Corridor(Tail):

    def __init__(self, *args, **kwargs):
        super(Corridor, self).__init__(*args, **kwargs)
        self.bread_crumbs = False
