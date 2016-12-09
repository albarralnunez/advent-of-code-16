import re
from libs import commons


class IPv7(object):

    ABBA_LENGTH = 4
    SSL_LENGTH = 3

    def __init__(self, ip):
        self.ip = ip
        self._aba = []
        self._bab = []

    @property
    def ip(self):
        return self._ip

    @ip.setter
    def ip(self, value):
        self._ip = value
        self._hypernet_sequences = re.findall(r'\[(\w+)\]', value)
        self._supernet_sequences = (
            re.findall(r'\](\w+)\[', value) +
            re.findall(r'(\w+)\[', value) +
            re.findall(r'\](\w+)', value)
        )

    @staticmethod
    def _take_groups(values, n):
        return (values[i:i+n] for i, _ in
                enumerate(values) if i+n < len(values)+1)

    @staticmethod
    def _is_abba(value):
        if value[0] == value[1]:
            return False
        return value[:2] == value[2:][::-1]

    @staticmethod
    def _is_aba_bab(value):
        return (value[0] != value[1] and
                value[1] != value[2] and
                value[0] == value[2])

    def has_tls(self):
        all_supernet_sequences = \
            commons.gflatten(self._take_groups(
                x, self.ABBA_LENGTH) for x in self._supernet_sequences)
        all_hypernet_sequences = \
            commons.gflatten(self._take_groups(
                x, self.ABBA_LENGTH) for x in self._hypernet_sequences)
        return (
            any(self._is_abba(sub) for sub in all_supernet_sequences) and
            all(not self._is_abba(sub) for sub in all_hypernet_sequences)
        )

    def has_ssl(self):
        all_supernet_sequences = \
            list(commons.gflatten(self._take_groups(
                x, self.SSL_LENGTH) for x in self._supernet_sequences))
        all_hypernet_sequences = \
            list(commons.gflatten(self._take_groups(
                x, self.SSL_LENGTH) for x in self._hypernet_sequences))
        abas = filter(lambda x: self._is_aba_bab(x), all_supernet_sequences)
        babs = filter(lambda x: self._is_aba_bab(x), all_hypernet_sequences)
        reversed_babs = list((x[1]+x[0]+x[1] for x in babs))
        a = set(abas) & set(reversed_babs)
        return len(list(a)) > 0
