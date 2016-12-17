

class Robot(object):

    def __init__(self, name):
        self.name = name
        self.microchips = {}

    def pick_microchip(self, microchip):
        self.microchips[microchip.value] = microchip

    def give_microchip(self, bot, microchip):
        own_micro = self.microchips.pop(microchip.value)
        bot.pick_microchip(own_micro)
