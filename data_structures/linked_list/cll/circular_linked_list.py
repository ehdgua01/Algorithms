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

    def connect_head_tail(self, node: Node = None):
        if node:
            self.head = node
            self.tail = node

        self.head.prev = self.tail
        self.tail.next = self.head

    def append(self, new: Node):
        if self.is_empty:
            self.connect_head_tail(new)
        else:
            self.tail.next = new
            new.prev = self.tail
            self.tail = new
            self.connect_head_tail()
        self.size += 1

    def insert(self, new: Node, location: int):
        if self.is_empty:
            self.connect_head_tail(new)
        else:
            target = self.get_node_at(location)
            new.prev = target
            new.next = target.next
            if self.tail == target:
                self.tail = new
                self.connect_head_tail()
            elif self.tail == target.next:
                self.tail.prev = new
            target.next = new
        self.size += 1

    def pop(self):
        if self.is_empty:
            raise ValueError("List is empty")
        self.tail = self.tail.prev
        self.connect_head_tail()
        self.size -= 1

    def remove(self, location: int):
        if self.is_empty:
            raise ValueError("List is empty")
        target = self.get_node_at(location)
        if self.tail == target:
            self.tail = self.tail.prev
            self.connect_head_tail()
        elif target.prev is not None:
            target.prev.next = target.next

        if location == 1:
            self.head = self.head.next
            self.connect_head_tail()

        self.size -= 1

    def get_node_at(self, location: int) -> Node:
        if (location < 1) or (self.size < location):
            raise ValueError("Invalid location")

        if int(self.size / 2) < location:
            target: Node = self.tail
            while self.size - location:
                target = target.prev
                location += 1
        else:
            target: Node = self.head
            while location > 1:
                target = target.next
                location -= 1

        return target

    def get_data_at(self, location: int):
        return self.get_node_at(location).data

    @property
    def is_empty(self) -> bool:
        return True if self.head is None else False
