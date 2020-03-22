class DivisionMethodHashTable(object):
    def __init__(self, initial_size: int) -> None:
        self._size = initial_size
        self._data = [None] * self._size

    def __setitem__(self, key: int, value) -> None:
        key = self.hash(key)

        if self._data[key] != value:
            self._data[key] = value

    def __getitem__(self, key: int):
        if isinstance(key, int):
            return self._data[self.hash(key)]
        else:
            raise TypeError

    def hash(self, value: int) -> int:
        value = value if value != 0 else self._size
        return value % self._size

    @property
    def size(self) -> int:
        return self._size
