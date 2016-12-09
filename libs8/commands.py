from libs.command import Command


class TurnOn(Command):

    def __init__(self, obj, x, y):
        super(TurnOn, self).__init__(obj)
        self._x = x
        self._y = y

    def execute(self, *args, **kwargs):
        self._obj.rect(self._x, self._y)


class RotateRow(Command):

    def __init__(self, obj, y, n):
        super(RotateRow, self).__init__(obj)
        self._y = y
        self._n = n

    def execute(self, *args, **kwargs):
        self._obj.rotate_row(self._y, self._n)


class RotateColumn(Command):

    def __init__(self, obj, x, n):
        super(RotateColumn, self).__init__(obj)
        self._x = x
        self._n = n

    def execute(self, *args, **kwargs):
        self._obj.rotate_column(self._x, self._n)
