class InvalidOrientation(Exception):
    pass


class CardinalPoints(object):

    CHOICES = ['N', 'W', 'S', 'E']

    def __init__(self, orientation='N'):
        if orientation not in self.CHOICES:
            message = 'Orientation must be one of this options {}'.format(
                self.CHOICES
            )
            raise InvalidOrientation(message)
        self._position = self.CHOICES.index(orientation)

    def __str__(self):
        return self.CHOICES[self._position]

    @property
    def position(self):
        return self.CHOICES[self._position]

    def turn_right(self):
        if self._position == 0:
            self._position = 3
        else:
            self._position -= 1

    def turn_left(self):
        if self._position == 3:
            self._position = 0
        else:
            self._position += 1
