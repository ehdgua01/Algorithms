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
            new.prev = self.tail
            self.tail = new

        self.size += 1

    def insert(self, new: Node, location: int):
        if (location < 1) or (self.size < location):
            raise ValueError('invalid location')

        if self.is_empty:
            self.head = new
            self.tail = new
        elif self.size == location:
            self.tail.next = new
            new.prev = self.tail
        else:
            """TODO
            location이 전체 사이즈의 절반보다 크면
            뒤에서 작으면 앞에서 시작하는 로직 추
            """
            temp = self.head
            while location > 1:
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
        if self.is_empty or location < 1:
            raise ValueError('List is empty')

        if self.size == location:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            """TODO
            location이 전체 사이즈의 절반보다 크면
            뒤에서 작으면 앞에서 시작하는 로직 추
            """
            temp = self.head
            while location > 1:
                temp = temp.next
                location -= 1
            temp.prev.next = temp.next
            temp.next = None

        self.size -= 1

    def get_data_at(self, location):
        if self.is_empty or (self.size < location) or (location < 1):
            raise ValueError('Invalid location')

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

        return target.data

    @property
    def is_empty(self):
        return True if self.head is None else False
