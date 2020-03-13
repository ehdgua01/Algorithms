class DigitsFoldingHashTable(object):
    def __init__(self, initial_size: int) -> None:
        self._size = initial_size
        self._data = [None] * self._size

    def __setitem__(self, key, value):
        key = self.hash(key)

        if self._data[key] != value:
            self._data[key] = value

    def __getitem__(self, key):
        if isinstance(key, str) or isinstance(key, int):
            return self._data[self.hash(key)]
        else:
            raise TypeError

    def hash(self, key):
        result = 0

        if isinstance(key, str):
            for c in str(key):
                result += ord(c)
        elif isinstance(key, int):
            for i in str(key):
                result += int(i)

        k = self.bit_count(result)
        s = self.bit_count(self._size)

        if k < s:
            result <<= (s - k)

        return result

    def bit_count(self, value) -> int:
        return len(bin(value).replace('0b', ''))
