import math
from typing import Any, Tuple


class PriorityQueue(object):
    def __init__(self):
        self.data = []

    def enqueue(self, value: Tuple[Any, int]):
        if not (isinstance(value, tuple) and isinstance(value[1], int)):
            raise TypeError

        self.data.append(value)
        current = self.size - 1
        parent = self.__get_parent(current)

        while current > 0 and self.data[current][1] < self.data[parent][1]:
            self.__swap(current, parent)
            current = parent
            self.__get_parent(current)

    def dequeue(self):
        if self.is_empty:
            return

        self.__swap(0, -1)
        result = self.data.pop()
        current = 0
        left = self.__get_left(current)
        right = self.__get_right(current)

        while left or right:
            if left and right:
                if (
                    self.data[left][1] < self.data[current][1]
                    or self.data[right][1] < self.data[current][1]
                ):
                    if self.data[left][1] <= self.data[right][1]:
                        self.__swap(current, left)
                        current = left
                    else:
                        self.__swap(current, right)
                        current = right
                else:
                    break
            elif left and self.data[left][1] < self.data[current][1]:
                self.__swap(current, left)
                current = left
            elif right and self.data[right][1] < self.data[current][1]:
                self.__swap(current, right)
                current = right
            else:
                break

            left = self.__get_left(current)
            right = self.__get_right(current)
        return result

    def __get_parent(self, child: int):
        if self.is_empty or child < 1:
            return None
        else:
            return math.floor((child - 1) / 2)

    def __get_left(self, index: int):
        left = (2 * index) + 1
        if self.size - 1 < left:
            return None
        else:
            return left

    def __get_right(self, index: int):
        right = (2 * index) + 2
        if self.size - 1 < right:
            return None
        else:
            return right

    def __swap(self, a: int, b: int) -> None:
        self.data[a], self.data[b] = self.data[b], self.data[a]

    @property
    def size(self) -> int:
        return len(self.data)

    @property
    def is_empty(self) -> bool:
        return self.size < 1
