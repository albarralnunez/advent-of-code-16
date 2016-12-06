#!/usr/local/bin/python
import logging
from collections import Counter
from libs import commons

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_messages(input_file):
    with open(input_file, 'r') as f:
        for line in f:
            yield line[:-1]


@commons.speed_test
def main():
    messages = get_messages('inputs/day_6.txt')
    most_common_letters = (Counter(x).most_common(1)[0][0] for x in zip(
        *messages))
    result = ''.join(most_common_letters)
    print 'Problem 1: The error-corrected version is: %s' % result
    messages = get_messages('inputs/day_6.txt')
    counters_for_each_index = (Counter(x) for x in zip(*messages))
    less_common_letters = (sorted(dict(cnt), key=(lambda x: cnt[x]))[0] for
                           cnt in counters_for_each_index)
    result = ''.join(x for x in less_common_letters)
    print 'Problem 2: The error-corrected version is: %s' % result

if __name__ == "__main__":
    main()
