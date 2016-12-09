#!/usr/local/bin/python
import logging
from libs import commons
from libs8.keypad import Keypad
from libs8.santa import Santa
from libs8.screen import Screen
from libs8.interpreter import Interpreter

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def read_input(input_file):
    with open(input_file, 'r') as f:
        actions = f.read().split('\n')
    return actions


@commons.speed_test
def main():
    actions = read_input('inputs/day_8.in')
    keypad = Keypad()
    screen = Screen(50, 6)
    santa = Santa(keypad=keypad, screen=screen, interpreter=Interpreter)
    for action in actions:
        santa.type(action)
    print 'Problem 1: The Number ' \
          'of pixels on are %s' % screen.number_pixels_on()
    print 'Problem 2: The screen displays << %s >>' % screen.decode()

if __name__ == "__main__":
    main()
