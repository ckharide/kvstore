class Memtable:

    def __init__(self, maxentries):
        self._entries = SortedDict
        self._maxsize = maxentries
