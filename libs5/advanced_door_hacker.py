import re
from libs5.door_hacker import DoorHacker
from libs5.exceptions import TooMuchIterations


class AdvancedDoorHacker(DoorHacker):

    def __init__(self, *args, **kwargs):
        super(AdvancedDoorHacker, self).__init__(*args, **kwargs)
        self._password = {}

    @property
    def password(self):
        if not self._decoded:
            raise ValueError('You should run decode before')
        return ''.join(self._password.values())

    @staticmethod
    def _has_valid_index(value):
        return re.match(r'[01234567]', value[5])

    def _already_exists(self, value):
        return int(value[5]) in self._password

    def decode(self):
        while len(self._password) < self._password_length:
            possible_hash = self._generate_hash(self._index)
            if (self._is_valid_hash(possible_hash) and
                    self._has_valid_index(possible_hash) and
                    not self._already_exists(possible_hash)):
                self._password[int(possible_hash[5])] = possible_hash[6]
            self._index += 1
        if self._index_out and self._index > self._index_out:
            raise TooMuchIterations('Too much iterations')
        self._decoded = True
