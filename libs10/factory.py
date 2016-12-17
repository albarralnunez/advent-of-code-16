from commands import Pick, Give

class Factory(object):

    def __init__(self, robot_type, micro_type, interpreter, console):
        self._robot_type = robot_type
        self._micro_type = micro_type
        self._interpreter = interpreter
        self._console = console
        self.robots = {}
        self.microchips = {}

    def get_or_create_robot(self, botname):
        robot = self.robots.get(botname)
        if not robot:
            robot = self._robot_type(name=botname)
            self.robots[botname] = robot
        return robot

    def get_or_create_micro(self, value):
        micro = self.microchips.get(value)
        if not micro:
            micro = self._micro_type(value=value)
            self.microchips[value] = micro
        return micro

    def find_bot_with_micro(self, micro_value):
        return self.microchips[micro_value].owner

    def run(self, action):
        interp = self._interpreter(action)
        comm = interp()
        command = comm[0]
        arrgs = comm[1]
        if command is Pick:
            bot = self.get_or_create_robot(arrgs['bot_name'])
            micro = self.get_or_create_micro(arrgs['micro_value'])
            self._console.execute(command(bot, micro))
            micro.owner = bot
        if command is Give:
            bot_origin = self.get_or_create_robot(arrgs['origin_bot_name'])
            bot_1 = self.get_or_create_robot(arrgs['desitny1_bot_name'])
            bot_2 = self.get_or_create_robot(arrgs['desitny2_bot_name'])
            micro1 = None
            micro2 = None
            if bot_origin.microchips:
                micro1 = bot_origin.microchips[min(bot_origin.microchips)]
            if len(bot_origin.microchips) > 1:
                micro2 = bot_origin.microchips[max(bot_origin.microchips)]
            if micro1:
                self._console.execute(command(bot_origin, bot_1, micro1))
                micro1.owner = bot_1
            if micro2:
                self._console.execute(command(bot_origin, bot_2, micro2))
                micro2.owner = bot_2
