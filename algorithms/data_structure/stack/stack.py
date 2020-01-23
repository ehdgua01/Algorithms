class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack(object):
    def __init__(self):
        self.top = None
        self.size = 0

    def pop(self):
        if self.is_empty:
            raise Exception('Stack is empty')
        data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return data

    def push(self, new: Node):
        if not isinstance(new, Node):
            raise TypeError('Not node type')
        if self.is_empty:
            self.top = new
        else:
            new.next = self.top
            self.top = new
        self.size += 1

    def peek(self):
        return None if self.is_empty else self.top.data

    def get_size(self):
        return self.size

    @property
    def is_empty(self):
        return self.top is None
