from libs2.command import Command


class MoveUp(Command):

    def execute(self, position):
        self._obj.move_up(position)


class MoveLeft(Command):

    def execute(self, position):
        self._obj.move_left(position)


class MoveRight(Command):

    def execute(self, position):
        self._obj.move_right(position)


class MoveDown(Command):

    def execute(self, position):
        self._obj.move_down(position)


class Press(Command):

    def execute(self, position):
        self._obj.press(position)
