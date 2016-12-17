#!/usr/local/bin/python
import logging
from libs import commons
from libs.point import Point
from libs13.maze import Maze

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def problem_1(m):
    start = m[Point(1, 1)]
    goal = m[Point(31, 39)]
    came_from, cost_so_far = m.a_star_search(start=start, goal=goal)
    path = m.reconstruct_path(came_from=came_from, start=start, goal=goal)
    for tail in path:
        tail.bread_crumbs = True
    print "Problem 1:\n\tThe fewest number of steps required" \
          "for going from (1, 1) to (31, 39) are %s" % (len(path)-1)
    print m


def problem_2(m):
    start = m[Point(1, 1)]
    tails, _ = m.find_all(start, steps=50)
    for tail in tails:
        tail.bread_crumbs = True
    print "Problem 2:\n\t Can reach in at most 50 " \
          "steps a total of %s tails" % (len(tails))
    print m


@commons.speed_test
def main():
    m = Maze(x=50, y=50, seed=1358)
    m.build()
    problem_1(m)
    m.release_the_bird_flock()
    problem_2(m)

if __name__ == '__main__':
    main()
