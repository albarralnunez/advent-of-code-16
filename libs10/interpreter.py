import re
from commands import Pick, Give


class Interpreter(object):

    INT = '[0-9]+'
    NAMES = '(?:bot)?(?:output)?'

    PICK = 'value ({}) goes to (bot {})'.format(INT, INT)
    GIVE = '(bot {}) gives low to ({} {}) and high to ({} {})'.format(
        INT, NAMES, INT, NAMES, INT)

    def __init__(self, command):
        self.command = command

    def __call__(self):
        match = re.match(self.PICK, self.command)
        if match:
            bot_name = match.group(2)
            micro_value = match.group(1)
            return Pick, {'bot_name': bot_name, 'micro_value': micro_value}
        match = re.match(self.GIVE, self.command)
        if match:
            origin_bot_name = match.group(1)
            desitny1_bot_name = match.group(2)
            desitny2_bot_name = match.group(3)
            return Give, {'origin_bot_name': origin_bot_name,
                          'desitny1_bot_name': desitny1_bot_name,
                          'desitny2_bot_name': desitny2_bot_name}
