from exceptions import MovementError


class Keypad:

    def __init__(self, keys):
        self._screen = ''
        self._keys = keys

    @property
    def screen(self):
        return self._screen

    @property
    def keys(self):
        return self._keys

    @keys.setter
    def keys(self, keys):
        if not keys and not keys[0]:
            ValueError('You must provide at least one key')
        self._keys = keys

    def __getitem__(self, key):
        return self._screen[key]

    def move_left(self, pointer):
        if (pointer.x - 1 < 0 or
                self.keys[pointer.y][pointer.x-1] == '*'):
            raise MovementError('Can not move left')
        else:
            pointer.x -= 1

    def move_right(self, pointer):
        if (pointer.x + 1 > len(self.keys[pointer.y]) - 1 or
                self.keys[pointer.y][pointer.x+1] == '*'):
            raise MovementError('Can not move right')
        else:
            pointer.x += 1

    def move_down(self, pointer):
        if (pointer.y + 1 > len(self.keys) - 1 or
                self.keys[pointer.y+1][pointer.x] == '*'):
            raise MovementError('Can not move down')
        else:
            pointer.y += 1

    def move_up(self, pointer):
        if (pointer.y - 1 < 0 or
                self.keys[pointer.y-1][pointer.x] == '*'):
            raise MovementError('Can not move up')
        else:
            pointer.y -= 1

    def press(self, pointer):
        value = self.keys[pointer.y][pointer.x]
        self._screen += value
