from libs.exceptions import WrongAction
from commands import TurnOn, RotateColumn, RotateRow


class Santa(object):
    """
    Should raise WrongFormat exception on action deciding
    """
    def __init__(self, keypad, screen, interpreter):
        self.interpreter = interpreter
        self.keypad = keypad
        self.screen = screen

    def type(self, action):
        inter = self.interpreter(action)
        comm = inter()
        self.keypad.execute(comm[0](self.screen, **comm[1]))
