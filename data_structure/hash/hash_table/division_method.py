class DivisionMethodHashTable(object):
    def __init__(self, initial_size: int) -> None:
        self._size = initial_size
        self._data = [None] * self._size

    def __setitem__(self, key: int, value) -> None:
        key = self.hash(key)

        if self[key] != value:
            self._data[key] = value

    def __getitem__(self, key: int):
        if isinstance(key, int):
            return self._data[self.hash(key)]
        else:
            raise TypeError

    def hash(self, value: int) -> int:
        value = value if value != 0 else self._size
        return value % self._size

    def is_prime(self, value: int) -> bool:
        if value in [0, 1, 2]:
            return True
        else:
            for i in range(2, value):
                if value % i == 0:
                    return False
            return True

    def next_prime(self, start: int) -> int:
        while not self.is_prime(start):
            start += 1
        return start

    def resize(self, new_size: int) -> None:
        if new_size < self._size:
            raise ValueError

        temp = {
            key: value
            for key, value in enumerate(self._data)
            if value is not None
        }
        self._size = self.next_prime(new_size)
        self._data = [None] * self._size

        for k, v in temp.items():
            self.__set(k, v)

    def __set(self, key, value) -> None:
        self[key] = value

    @property
    def size(self) -> int:
        return self._size
