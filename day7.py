#!/usr/local/bin/python
import logging
from collections import Counter
from libs import commons
from libs7.ipv7 import IPv7

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_ips(input_file):
    return (IPv7(x[:-1]) for x in open(input_file, 'r').xreadlines())


@commons.speed_test
def problem_1(ips):
    return len(filter(lambda x: x.has_tls(), ips))


@commons.speed_test
def problem_2(ips):
    return len(filter(lambda x: x.has_ssl(), ips))


def main():
    ips = get_ips('inputs/day_7.in')
    print 'Problem 1: %s IPs supports TLS' % problem_1(ips)
    ips = get_ips('inputs/day_7.in')
    print 'Problem 2: %s IPs supports SSL' % problem_2(ips)

if __name__ == "__main__":
    main()
