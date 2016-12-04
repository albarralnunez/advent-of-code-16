class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Point(%s,%s)" % (self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

    def tc_distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return dx + dy

    def tuple(self):
        return self.x, self.y
