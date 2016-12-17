import re


class Assembunny(object):

    REG_OR_INT = '((?:-?[0-9]+)?(?:[abcd])?)'
    INT = '(-?[0-9]+)'
    REG = '([abcd])'
    SPC = ' '
    CPY = r'cpy' + SPC + REG_OR_INT + SPC + REG
    INC = r'inc' + SPC + REG
    DEC = r'dec' + SPC + REG
    JNZ = r'jnz' + SPC + REG_OR_INT + SPC + REG_OR_INT

    def __init__(self, operations, reg_state=None):
        self.reg = reg_state
        if not self.reg:
            self.reg = {
                'a': 0,
                'b': 0,
                'c': 0,
                'd': 0
            }
        self._ops = operations
        self._index = 0

    def get_reg_or_int(self, x):
        try:
            return int(x)
        except ValueError:
            return self.reg[x]

    def _exe(self, op):
        m = re.match(self.CPY, op)
        if m:
            x = m.group(1)
            y = m.group(2)
            self.reg[y] = self.get_reg_or_int(x)
            self._index += 1
        m = re.match(self.INC, op)
        if m:
            x = m.group(1)
            self.reg[x] += 1
            self._index += 1
        m = re.match(self.DEC, op)
        if m:
            x = m.group(1)
            self.reg[x] -= 1
            self._index += 1
        m = re.match(self.JNZ, op)
        if m:
            x = m.group(1)
            y = m.group(2)
            if self.get_reg_or_int(x):
                self._index += self.get_reg_or_int(y)
            else:
                self._index += 1

    def run(self):
        while self._index < len(self._ops):
            self._exe(self._ops[self._index])


