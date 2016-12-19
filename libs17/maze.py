import hashlib
from libs.point import Point
from libs.graph.graph import Graph
from libs.graph.non_linear_search_mixin import NonLinearSearchMixin
from libs17.tails import Corridor


class Maze(Graph, NonLinearSearchMixin):

    def __init__(self, x, y, key):
        self.x = x
        self.y = y
        self.key = key
        self.maze = {}

    def __repr__(self):
        rep = ''
        for y in range(self.y):
            for x in range(self.x):
                if self.maze[Point(x, y)].bread_crumbs:
                    rep += '0'
                else:
                    rep += '.'
            rep += '\n'
        return rep

    def __getitem__(self, item):
        return self.maze[item]

    @property
    def _graph(self):
        return self.maze

    def heuristic(self, a, b):
        return abs(a.tail_id.x - b.tail_id.x) + abs(a.tail_id.y - b.tail_id.y)

    def movement_cost(self, a, b):
        key = hashlib.md5(self.key)[:4]
        if a.tail_id.x > b.tail_id.x:


    def _init_maze(self):
        for x in range(self.x):
            for y in range(self.y):
                corridor = Corridor(Point(x, y))
                self.maze[corridor.tail_id] = corridor

    def _connect_maze(self):
        for point in self.maze:
            tail = self.maze[point]
            if point.x+1 < self.x:
                tail.r = self.maze[Point(point.x+1, point.y)]
            if point.x-1 >= 0:
                tail.l = self.maze[Point(point.x-1, point.y)]
            if point.y+1 < self.y:
                tail.u = self.maze[Point(point.x, point.y+1)]
            if point.y-1 >= 0:
                tail.d = self.maze[Point(point.x, point.y-1)]

    def build(self):
        self._init_maze()
        self._connect_maze()

    def release_the_bird_flock(self):
        for point in self.maze:
            if (isinstance(self.maze[point], Corridor) and
                    self.maze[point].bread_crumbs):
                self.maze[point].bread_crumbs = False
