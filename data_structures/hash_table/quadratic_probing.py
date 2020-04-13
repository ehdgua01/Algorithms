from typing import List, Union
from math import floor, sqrt


class QuadraticProbingHashTable(object):
    def __init__(self, initial_size: int):
        self.__size = initial_size
        self.__keys = {}
        self.__data: List[Union[int, None]] = [None] * self.__size

    def hash(self, value: int) -> int:
        value = value if value != 0 else self.__size
        return value % self.__size

    def is_prime(self, number: int) -> bool:
        if number <= 1:
            return False
        elif number == 2:
            return True
        elif 2 < number and number % 2 == 0:
            return False

        max_div = floor(sqrt(number))
        for i in range(3, 1 + max_div, 2):
            if number % i == 0:
                return False
        return True

    def next_prime(self, start: int) -> int:
        start += 1
        while not self.is_prime(start):
            start += 1
        return start

    def rehashing(self, new_size: int) -> None:
        if new_size < self.__size:
            raise ValueError
        elif not self.is_prime(new_size):
            new_size = self.next_prime(new_size)

        temp = [value for value in self.__data if isinstance(value, int)]
        self.__keys.clear()
        self.__size = new_size
        self.__data = [None] * self.__size
        [self.set(v) for v in temp]

    def set(self, value: int, key=None, **kwargs) -> None:
        if not isinstance(value, int):
            raise TypeError

        key = self.hash(key or value)

        if self.__data[key] is None:
            self.__data[key] = value
            self.__keys[key] = value
        elif self.__data[key] == value:
            return
        else:
            if self.usage > 0.75:
                self.rehashing(self.next_prime(self.__size))
                self.set(value)
            else:
                coefficient = kwargs.get("coefficient", 0) + 1
                self.set(value, key + (coefficient ** 2), coefficient=coefficient)

    @property
    def keys(self):
        return self.__keys

    @property
    def size(self) -> int:
        return self.__size

    @property
    def usage(self):
        return round(sum(1 for v in self.__data if v is not None) / self.__size, 2)
