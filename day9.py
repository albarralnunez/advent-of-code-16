#!/usr/local/bin/python
import logging
from libs import commons
from libs9.decompressor import Decompressor

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def read_input(input_file):
    with open(input_file, 'r') as f:
        loaded_file = f.read()
    return loaded_file


@commons.speed_test
def main():
    loaded_file = read_input('inputs/day_9.txt')
    decompressed = Decompressor(file=loaded_file)
    print 'Problem 1: The decompressed length are %s' % len(
        filter(lambda x: x != ' ', decompressed()))

if __name__ == "__main__":
    main()
