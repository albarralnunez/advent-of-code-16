from commands import (MoveUp, MoveDown, MoveLeft, MoveRight, Press)
from libs.exceptions import WrongAction


class BathroomUser(object):

    def __init__(self, keypad, finger):
        self._keypad = keypad
        self._finger = finger

    @property
    def keypad(self):
        return self._keypad

    @keypad.setter
    def keypad(self, keypad):
        self._keypad = keypad

    def move_finger(self, action):
        if action == 'U':
            command = MoveUp(self._keypad)
        elif action == 'D':
            command = MoveDown(self._keypad)
        elif action == 'L':
            command = MoveLeft(self._keypad)
        elif action == 'R':
            command = MoveRight(self._keypad)
        elif action == 'P':
            command = Press(self._keypad)
        else:
            raise WrongAction('You can only preform the following actions: '
                              'U, D, L, R, P. %s was preformed' % action)
        self._finger.execute(command)
