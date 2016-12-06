#!/usr/local/bin/python
from libs.commons import speed_test
from libs.point import Point
from libs1.path import Path


def read_input(input_file):
    with open(input_file, 'r') as f:
        actions = f.read().split(', ')
    return actions


def problem_1(actions):
    path = Path()
    for action in actions:
        path.move(action)
    return path.position.point.tc_distance(Point(0, 0))


def problem_2(actions):
    path = Path()
    for action in actions:
        path.move(action)
        if len(path.intersections) > 0:
            break
    if path.intersections:
        return path.intersections[0].tc_distance(Point(0, 0))
    return path.position.point.tc_distance(Point(0, 0))


@speed_test
def main():
    actions = read_input('inputs/day_1.in')
    print 'Taxicap distance: %s' % problem_1(actions)
    print 'Taxicap distance to first intersection: %s' % problem_2(actions)


if __name__ == "__main__":
    main()
