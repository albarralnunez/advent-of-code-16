import copy

from libs1.position import Position


class Path(object):

    def __init__(self):
        self.path = {(0, 0): 1}
        self.position = Position()
        self.intersections = []

    def move(self, action):
        if action[0] == 'L':
            self.position.turn_left()
        if action[0] == 'R':
            self.position.turn_right()
        for _ in range(int(action[1:])):
            self.position.move(1)
            cnt = self.path.get(self.position.point.tuple(), 0)
            if cnt == 1:
                self.intersections.append(copy.copy(self.position.point))
            self.path.update({self.position.point.tuple(): cnt+1})
