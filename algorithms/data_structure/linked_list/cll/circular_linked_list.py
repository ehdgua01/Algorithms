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

    def init(self, new: Node):
        self.head = new
        self.tail = new
        self.head.prev = self.tail
        self.tail.next = self.head

    def append(self, new: Node):
        if self.is_empty:
            self.init(new)
        else:
            self.tail.next = new
            new.prev = self.tail
            self.tail = new
            self.tail.next = self.head
        self.size += 1

    @property
    def is_empty(self):
        return True if self.head is None else False
