from libs.command import Command


class Pick(Command):

    def __init__(self, obj, x):
        super(Pick, self).__init__(obj)
        self._x = x

    def execute(self, *args, **kwargs):
        self._obj.pick_microchip(self._x)


class Give(Command):

    def __init__(self, obj, to, x):
        super(Give, self).__init__(obj)
        self._x = x
        self._to = to

    def execute(self, *args, **kwargs):
        self._obj.give_microchip(self._to, self._x)
