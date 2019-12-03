class Node(object):
    next = None
    prev = None

    def __init__(self, data):
        self.data = data


class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, new: Node):
        if self.is_empty:
            self.head = new
            self.tail = new
        else:
            old_tail = self.tail
            new.prev = old_tail
            old_tail.next = self.tail

        self.size += 1

    def insert(self, new: Node, location: int):
        if (location < -1) or (location > self.size):
            raise ValueError('invalid location')

        if self.is_empty:
            self.head = new
            self.head.next = new
            self.tail = new
        elif location == -1 or self.size == location:
            self.tail.next = new
            new.prev = self.tail
        else:
            temp = self.head
            while location:
                temp = temp.next
                location -= 1
            new.next = temp.next
            new.prev = temp
            temp.next = new

        self.size += 1

    def pop(self):
        if self.is_empty:
            raise ValueError('List is empty')
        self.tail = self.tail.prev
        self.tail.next = None
        self.size -= 1

    def remove(self, location):
        if self.is_empty:
            raise ValueError('List is empty')

        if location == -1 or self.size == location:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            temp = self.head
            while location:
                temp = temp.next
                location -= 1
            temp = temp.prev
            temp.next = None

    @property
    def is_empty(self):
        return True if self.head is None else False
