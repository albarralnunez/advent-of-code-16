class Command(object):
    """The COMMAND interface"""
    def __init__(self, obj):
        self._obj = obj

    def execute(self, *args, **kwargs):
        raise NotImplementedError
