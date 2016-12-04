
class Finger(object):

    def __init__(self, point):
        self._position = point

    def execute(self, command):
        command.execute(self._position)
