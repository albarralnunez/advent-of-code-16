import re
from exceptions import UniqueError


class Bank(object):

    def __init__(self, rooms):
        self.rooms = rooms

    @property
    def rooms(self):
        return self._rooms.values()

    @rooms.setter
    def rooms(self, rooms):
        self._rooms = rooms
        if not rooms:
            self._rooms = {}

    def get(self, key):
        return self._rooms[key]

    def add(self, room):
        exists_room = self._rooms.get(room.name)
        if exists_room:
            raise UniqueError('The room name already exists.')
        self._rooms[room.name] = room

    def find_similar(self, similar):
        regex = r'.*%s.*' % similar
        return filter(lambda x: re.match(regex, x), self._rooms.keys())
