import collections


class Room(object):

    def __init__(self, name, sector, checksum):
        self.name = name
        self.sector = sector
        self.checksum = checksum

    def __str__(self):
        return self._name, self._sector

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def sector(self):
        return self._sector

    @sector.setter
    def sector(self, sector):
        self._sector = sector

    @property
    def checksum(self):
        return self._checksum

    @checksum.setter
    def checksum(self, checksum):
        self._checksum = checksum

    def validate(self):
        if not self.name or not self.sector or not self.checksum:
            raise ValueError('name, sector and checksum must be provided in '
                             'order to validate the room.')
        clean_name = self._name.replace(' ', '')
        name_letters = collections.Counter(clean_name).most_common()
        name_letters.sort(key=lambda y: (-y[1], y[0]))
        expected_checksum = ''.join([x[0] for x in name_letters[:5]])
        return expected_checksum == self._checksum
