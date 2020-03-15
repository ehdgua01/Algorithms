class Node(object):
    def __init__(self, key, value) -> None:
        self.next = None
        self.key = key
        self.value = value


class LinkedListHashTable(object):
    def __init__(self, initial_size) -> None:
        self._size = initial_size
        self._data = [Node(None, None)] * self._size

    def __setitem__(self, key: int, value) -> None:
        if not isinstance(key, int):
            raise TypeError

        target = self._data[self.hash(key)]

        while target.next is not None:
            target = target.next
            if target.key == key:
                target.value = value
                return

        new_node = Node(key, value)
        target.next = new_node

    def __getitem__(self, key: int):
        if not isinstance(key, int):
            raise TypeError

        target = self._data[self.hash(key)]

        while target.next is not None:
            target = target.next
            if target.key == key:
                return target.value
        return None

    def hash(self, value) -> int:
        value = value if value != 0 else self.size
        return value % self._size

    @property
    def size(self) -> int:
        return self._size
