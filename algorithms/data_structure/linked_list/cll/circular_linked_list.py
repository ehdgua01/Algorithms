class Node(object):
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data


class CircularLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, new: Node):
        if self.is_empty:
            self.head = new
            self.tail = new
            self.head.prev = self.tail
            self.tail.next = self.head
        else:
            self.tail.next = new
            new.prev = self.tail
            self.tail = new
            self.tail.next = self.head

        self.size += 1

    @property
    def is_empty(self):
        return True if self.head is None else False
