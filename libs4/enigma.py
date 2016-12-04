import re
from exceptions import WrongFormat


class Enigma(object):

    ID_FORMAT = r'([a-z\-]+)-+([0-9]+)\[([a-z]+)\]'

    def __init__(self, room_id, encryption, room):
        self.room_id = room_id
        self.encryption = encryption
        self.room = room

    @property
    def room_id(self):
        return self._room_id

    @room_id.setter
    def room_id(self, room_id):
        self._room_id = room_id

    @property
    def encryption(self):
        return self._encryption

    @encryption.setter
    def encryption(self, encryption):
        self._encryption = encryption

    @property
    def room(self):
        return self._room

    @room.setter
    def room(self, room):
        self._room = room

    def translate(self):
        room_id_grouped = re.match(self.ID_FORMAT, self._room_id)
        if not room_id_grouped:
            raise WrongFormat(
                'The room id must match with this regex %s' % self._id_format)
        name = room_id_grouped.group(1).replace('-', ' ')
        sector = int(room_id_grouped.group(2))
        checksum = room_id_grouped.group(3)
        decrypter = self._encryption(name, sector)
        return self._room(name=decrypter.decode(), sector=sector,
                          checksum=checksum)
