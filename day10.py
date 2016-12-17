#!/usr/local/bin/python
import logging
from libs import commons
from libs10.console import Console
from libs10.factory import Factory
from libs10.interpreter import Interpreter
from libs10.robot import Robot
from libs10.microchip import Microchip


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def read_input(input_file):
    with open(input_file, 'r') as f:
        actions = f.read().split('\n')
    return actions


@commons.speed_test
def main():
    commands = read_input('inputs/day_10.in')
    factory = Factory(robot_type=Robot, micro_type=Microchip,
                      interpreter=Interpreter, console=Console)
    for command in commands:
        factory.run(command)
    res1 = factory.find_bot_with_micro('61')
    print 'Problem 1: The robot is %s' % res1.name

if __name__ == "__main__":
    main()
