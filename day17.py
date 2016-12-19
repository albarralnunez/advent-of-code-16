#!/usr/local/bin/python
import logging
from libs import commons
from libs.point import Point
from libs17.maze import Maze

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def problem_1(m):
    start = m[Point(0, 0)]
    goal = m[Point(3, 3)]
    print 'Start search...'
    came_from, cost_so_far = m.non_linear_search(start=start, goal=goal)
    print came_from
    print 'Search ended...'
    print 'Retrieving path...'
    path = m.reconstruct_path(came_from=came_from, start=start, goal=goal)
    for tail in path:
        tail.bread_crumbs = True
    print "Problem 1:\n\tThe shortest path is %s" % (len(path)-1)
    print m


@commons.speed_test
def main():
    m = Maze(x=4, y=4, key='pxxbnzuo')
    m.build()
    problem_1(m)
    m.release_the_bird_flock()

if __name__ == '__main__':
    main()
