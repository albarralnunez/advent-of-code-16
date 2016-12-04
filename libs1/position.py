from libs1.cardinal_points import CardinalPoints
from libs.point import Point


class Position(object):

    def __init__(self, x=0, y=0, orientation='N'):
        self.orientation = CardinalPoints(orientation)
        self.point = Point(x, y)

    def __str__(self):
        return 'Orientation {}, Position {}'.format(
            self.orientation, self.point)

    def move(self, steps):
        if self.orientation.position == 'N':
            self.point.move(0, steps)
        if self.orientation.position == 'W':
            self.point.move(-steps, 0)
        if self.orientation.position == 'S':
            self.point.move(0, -steps)
        if self.orientation.position == 'E':
            self.point.move(steps, 0)

    def turn_left(self):
        self.orientation.turn_left()

    def turn_right(self):
        self.orientation.turn_right()
