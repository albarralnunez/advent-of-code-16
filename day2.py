#!/usr/local/bin/python
import logging
from libs.commons import speed_test
from libs.point import Point
from libs2.keypad import Keypad
from libs2.bathroom_user import BathroomUser
from libs2.finger import Finger
from libs2.exceptions import MovementError


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def read_input(input_file):
    with open(input_file, 'r') as f:
        actions = f.read().split('\n')
    return actions


def problem(actions, keys, start_point):
    keypad = Keypad(keys)
    finger = Finger(start_point)
    santa = BathroomUser(keypad, finger)
    for action in actions:
        for move in action:
            try:
                santa.move_finger(move)
            except Exception as ex:
                pass
        santa.move_finger('P')
    return keypad.screen


@speed_test
def main():
    problem_1_keys = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9']
    ]
    problem_1_start = Point(1, 1)
    problem_2_keys = [
        ['*', '*', '1', '*', '*'],
        ['*', '2', '3', '4', '*'],
        ['5', '6', '7', '8', '9'],
        ['*', 'A', 'B', 'C', '*'],
        ['*', '*', 'D', '*', '*']
    ]
    problem_2_start = Point(0, 2)
    actions = read_input('inputs/day_2.in')
    print 'Problem 1 Password: %s' % problem(
        actions, problem_1_keys, problem_1_start)
    print 'Problem 2 Password: %s' % problem(
        actions, problem_2_keys, problem_2_start)


if __name__ == "__main__":
    main()
