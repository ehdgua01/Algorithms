class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedQueue(object):
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def put(self, node: Node) -> None:
        if self.is_empty:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node
        self.size += 1

    def get(self):
        if self.is_empty:
            raise Exception
        value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        return value

    @property
    def is_empty(self) -> bool:
        return self.size < 1
