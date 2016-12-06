#!/usr/local/bin/python
import logging
import re
from libs import commons
from libs3.triangle import Triangle


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def read_input_problem_1(input_file):
    with open(input_file, 'r') as f:
        lines = f.read().split('\n')
    triangle_list = [re.findall(r'\d+', line) for line in lines]
    triangles = [Triangle(int(c1), int(c2), int(h))
                 for c1, c2, h in triangle_list]
    return triangles


def read_input_problem_2(input_file):
    with open(input_file, 'r') as f:
        lines = f.read().split('\n')
    triangle_list = [re.findall(r'\d+', line) for line in lines]
    rotated = [zip(a, b, c) for a, b, c in commons.chunks(triangle_list, 3)]
    triangles = [Triangle(int(c1), int(c2), int(h))
                 for c1, c2, h in commons.flatten(rotated)]
    return triangles


def problem(triangles):
    return len(filter(lambda x: x.is_valid(), triangles))


@commons.speed_test
def main():
    triangles = read_input_problem_1('inputs/day_3.in')
    print 'Problem 1 Number of valid triangles: %s' % problem(triangles)
    triangles = read_input_problem_2('inputs/day_3.in')
    print 'Problem 2 Number of valid triangles: %s' % problem(triangles)

    # Epic one liner for problem one
    with open('inputs/day_3.in', 'r') as f:
        print 'Problem 1 Number of valid triangles: %s' % len(filter(
            lambda x: x.is_valid(),
            [Triangle(int(c1), int(c2), int(h))
             for c1, c2, h in [re.findall(r'\d+', line)
                               for line in f.read().split('\n')]]))

    # Epic one liner for problem two
    with open('inputs/day_3.in', 'r') as f:
        print 'Problem 2 Number of valid triangles: %s' % len(filter(
            lambda x: x.is_valid(),
            [Triangle(int(c1), int(c2), int(h))
             for c1, c2, h in
             [item for sublist in
              [zip(a, b, c) for a, b, c in
               commons.chunks([re.findall(r'\d+', line) for line in
                               f.read().split('\n')], 3)] for item in sublist]]
        ))

if __name__ == "__main__":
    main()
