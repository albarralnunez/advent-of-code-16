from libs.point import Point
from tails import Corridor, Wall
from graph import Graph


class Maze(Graph):

    def __init__(self, x, y, seed):
        self.x = x
        self.y = y
        self.seed = seed
        self.maze = {}

    def __repr__(self):
        rep = ''
        for y in range(self.y):
            for x in range(self.x):
                if isinstance(self.maze[Point(x, y)], Corridor):
                    if self.maze[Point(x, y)].bread_crumbs:
                        rep += '0'
                    else:
                        rep += '.'
                else:
                    rep += '+'
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
        return 1

    def _init_maze(self):
        for x in range(self.x):
            for y in range(self.y):
                origin = (x * x + 3 * x + 2 * x * y + y + y * y) + self.seed
                # Find the binary representation of origin; count the
                # number of bits that are 1
                conditioner = len(
                    filter(lambda val: int(val) == 1, bin(origin)[2:]))
                if conditioner % 2 == 0:
                    corridor = Corridor(Point(x, y))
                    self.maze[corridor.tail_id] = corridor
                else:
                    wall = Wall(Point(x, y))
                    self.maze[wall.tail_id] = wall

    def _connect_maze(self):
        for point in self.maze:
            tail = self.maze[point]
            if point.x+1 < self.x:
                tail.e = self.maze[Point(point.x+1, point.y)]
            if point.x-1 >= 0:
                tail.w = self.maze[Point(point.x-1, point.y)]
            if point.y+1 < self.y:
                tail.n = self.maze[Point(point.x, point.y+1)]
            if point.y-1 >= 0:
                tail.s = self.maze[Point(point.x, point.y-1)]

    def build(self):
        self._init_maze()
        self._connect_maze()

    def release_the_bird_flock(self):
        for point in self.maze:
            if (isinstance(self.maze[point], Corridor) and
                    self.maze[point].bread_crumbs):
                self.maze[point].bread_crumbs = False
