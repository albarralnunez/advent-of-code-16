#!/usr/local/bin/python
import logging
import hashlib
from libs import commons
from libs5.door_hacker import DoorHacker
from libs5.advanced_door_hacker import AdvancedDoorHacker

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@commons.speed_test
def problem1(door_id):
    door_hacker = DoorHacker(
        password_length=8, code=door_id, algorithm=hashlib.md5)
    door_hacker.decode()
    return door_hacker.password


@commons.speed_test
def problem2(door_id):
    door_hacker = AdvancedDoorHacker(
        password_length=8, code=door_id, algorithm=hashlib.md5)
    door_hacker.decode()
    return door_hacker.password


def main():
    door_id = "ugkcyxxp"
    print 'Problem 1: The password is: %s' % problem1(door_id)
    print 'Problem 2: The password is: %s' % problem2(door_id)


if __name__ == "__main__":
    main()
