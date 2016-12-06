#!/usr/local/bin/python
import logging
from libs import commons
from libs4.room import Room
from libs4.encoder import DummyEncoder
from libs4.caesar_cipher import CaesarCipher
from libs4.bank import Bank
from libs4.enigma import Enigma

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def read_input_problem_2(input_file):
    bank = Bank({})
    with open(input_file, 'r') as f:
        for line in f:
            translator = Enigma(
                room_id=line, room=Room, encryption=CaesarCipher)
            room = translator.translate()
            bank.add(room)
    return bank


def read_input_problem_1(input_file):
    bank = Bank({})
    with open(input_file, 'r') as f:
        for line in f:
            translator = Enigma(
                room_id=line, room=Room, encryption=DummyEncoder)
            room = translator.translate()
            bank.add(room)
    return bank


def problem1(bank):
    valid_rooms = filter(lambda r: r.validate(), bank.rooms)
    return sum(x.sector for x in valid_rooms)


def problem2(bank):
    similar1 = bank.find_similar('north')
    similar2 = bank.find_similar('pole')
    similar = list(set(similar1) & set(similar2))
    if similar:
        room = bank.get(similar[0])
        return room.sector
    return -1


@commons.speed_test
def main():
    bank = read_input_problem_1('inputs/day_4.in')
    print 'Problem 1: Sum of the sector IDs of the real rooms: %s' % \
          problem1(bank)
    bank = read_input_problem_2('inputs/day_4.in')
    print 'Problem 2: Sector ID of the room where' \
          'North Pole objects are stored %s' % problem2(bank)

if __name__ == "__main__":
    main()
