class Node(object):
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.pointer = None
        self.size = 0

    def __repr__(self):
        return f'<LinkedList head={self.head} tail={self.tail}>'

    def clear(self):
        self.__init__()

    def is_empty(self):
        return True if not self.size else False

    def append(self, new: Node):
        if self.is_empty():
            self.head = new
            self.tail = new
            self.pointer = self.head

        else:
            self.tail = self.head

            while self.tail.next_node is not None:
                self.tail = self.tail.next_node

            self.tail.next_node = new
            self.tail = new
        self.size += 1

    def insert(self, new: Node, is_head=False):
        if self.is_empty():
            self.head = new
            self.tail = new
            self.pointer = self.head

        else:
            if is_head:
                new.next_node = self.head
                self.head = new

            else:
                if self.pointer.next_node is None:
                    self.tail = new

                new.next_node = self.pointer.next_node
                self.pointer.next_node = new
        self.size += 1

    def pop(self):
        if self.is_empty():
            return None

        self.tail = self.head

        while self.tail.next_node is not None:
            self.pointer = self.tail
            self.tail = self.tail.next_node

        try:
            return self.pointer.next_node.data
        finally:
            self.pointer.next_node = None
            self.tail = self.pointer
            self.size -= 1

    def remove(self, remove: Node):
        if self.is_empty():
            return None

        if remove == self.head:
            self.head = remove.next_node

        else:
            self.pointer = self.head

            while self.pointer is not None and self.pointer.next_node != remove:
                self.pointer = self.pointer.next_node

            if self.pointer is not None:
                self.pointer.next_node = remove.next_node
            else:
                self.pointer = self.head

        self.size -= 1

    def next(self):
        if self.is_empty() or not self.pointer.next_node:
            print('다음 노드가 존재하지 않습니다.')
            return None

        self.pointer = self.pointer.next_node
        return self.pointer.data

    def move_to_head(self):
        self.pointer = None if self.is_empty() else self.head

    def move_to_tail(self):
        self.pointer = None if self.is_empty() else self.tail
