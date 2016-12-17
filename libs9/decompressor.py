

class Decompressor(object):

    def __init__(self, file):
        self._file = file
        self._stack = [0]
        self._index = 0
        self._decoded = ''

    def _take_marker(self):
        self._index += 1
        x = ''
        y = ''
        while self._file[self._index] != 'x':
            x += self._file[self._index]
            self._index += 1
        self._index += 1
        while self._file[self._index] != ')':
            y += self._file[self._index]
            self._index += 1
        self._index += 1
        self._stack.append(int(y))
        self._stack.append(int(x))

    def _take_str(self, x, y):
        g = ''
        while x:
            g += self._file[self._index]
            self._index += 1
            x -= 1
        self._decoded += g * y

    def _ignore_marker(self):
        while self._file[self._index] != ')':
            self._decoded += self._file[self._index]
            self._index += 1
        self._decoded += self._file[self._index]

    def __call__(self, *args, **kwargs):
        self._index = 0
        while self._index < len(self._file):
            if self._file[self._index] == '(' and self._stack[-1] == 0:
                self._take_marker()
            else:  # self._file[self._index] != '(':
                iter = self._stack.pop()
                if not iter:
                    self._stack.append(0)
                    self._decoded += self._file[self._index]
                    self._index += 1
                else:
                    mul = self._stack.pop()
                    self._take_str(iter, mul)
        self._index = 0
        return self._decoded
