import unittest

from libs.commons import speed_test
from libs13.maze import Maze
from libs13 import graph


class TestMaze(unittest.TestCase):

    @speed_test
    def test_move(self):
        m = Maze(x=10, y=7, seed=10)
        m.build()
        print m
        start = m[(1, 1)]
        goal = m[(7, 4)]
        came_from, cost_so_far = graph.a_star_search(
            m, start=start, goal=goal)
        path = graph.reconstruct_path(
            came_from=came_from, start=start, goal=goal)
        for tail in path:
            tail.bread_crumbs = True
        print m
        print [(tail.x, tail.y) for tail in path]
        self.assertEqual(len(path) - 1, 11)

if __name__ == '__main__':
    unittest.main()
