import re
from exceptions import WrongFormat
from commands import TurnOn, RotateColumn, RotateRow


class Interpreter(object):

    ROTATE_AC = 'rotate'
    RECT_AC = 'rect'
    COL = 'column'
    ROW = 'row'
    EQ = '='
    X = 'x'
    Y = 'y'
    BY = 'by'
    INT = '([0-9]+)'
    SPA = '\ '

    RECT = INT + X + INT

    ROTATE_ROW = (ROTATE_AC + SPA + ROW + SPA +
                  Y + EQ + INT + SPA + BY + SPA + INT)
    ROTATE_COL = (ROTATE_AC + SPA + COL + SPA + X +
                  EQ + INT + SPA + BY + SPA + INT)
    ON_RECT = RECT_AC + SPA + RECT

    def __init__(self, command):
        self.command = command

    def __call__(self):

        match = re.match(self.ON_RECT, self.command)
        if match:
            x = match.group(1)
            y = match.group(2)
            return TurnOn, {'x': int(x), 'y': int(y)}
        match = re.match(self.ROTATE_COL, self.command)
        if match:
            x = match.group(1)
            n = match.group(2)
            return RotateColumn, {'x': int(x), 'n': int(n)}
        match = re.match(self.ROTATE_ROW, self.command)
        if match:
            y = match.group(1)
            n = match.group(2)
            return RotateRow, {'y': int(y), 'n': int(n)}
        raise WrongFormat(self.command)
