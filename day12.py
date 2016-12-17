#!/usr/local/bin/python
import logging
from libs import commons
from libs12.assembunny import Assembunny

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def read_input(input_file):
    with open(input_file, 'r') as f:
        comm = f.read().split('\n')
    return comm


@commons.speed_test
def main():
    commands = read_input('inputs/day_12.asb')
    ass = Assembunny(operations=commands)
    ass.run()
    print 'Problem 1: The registers have the values %s' % ass.reg
    ass = Assembunny(operations=commands, reg_state={'a': 0, 'b': 0,
                                                     'c': 1, 'd': 0})
    ass.run()
    print 'Problem 2: The registers have the values %s' % ass.reg


if __name__ == '__main__':
    main()