import math


class Heap(object):
    def __init__(self):
        self.size = 0
        self.data = []

    def insert(self, value):
        self.data.append(value)
        current = self.size
        self.size += 1
        parent = self.get_parent(current)

        while current > 0 and self.data[current] < self.data[parent]:
            self.data[current], self.data[parent] = (
                self.data[parent],
                self.data[current],
            )
            current = parent
            self.get_parent(current)

    def get_parent(self, child: int):
        if child > 2:
            return math.floor((child - 1) / 2)
        elif child < 1:
            return None
        else:
            return 0

    def get_data(self, index: int):
        if self.is_empty:
            return
        else:
            return self.data[index]

    @property
    def is_empty(self):
        return self.size < 0
