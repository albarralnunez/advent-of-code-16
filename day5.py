#!/usr/local/bin/python
import logging
from libs import commons

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

"""
    I will reuse the Encoder class used in problem of day4 for decrypt the pass
    of the door.
"""


def problem1(door_id):
    pass


@commons.speed_test
def main():
    door_id = "ugkcyxxp"
    print 'Problem 1: The password is: %s' % problem1(door_id)

if __name__ == "__main__":
    main()
