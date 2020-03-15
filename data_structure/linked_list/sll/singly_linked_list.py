class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, new: Node):
        if self.is_empty:
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            self.tail = new
        self.size += 1

    def insert(self, new: Node, location: int):
        if location < 1 or (self.is_empty and location != 1):
            raise ValueError("invalid location")

        if self.is_empty:
            self.head = new
            self.tail = new
        else:
            target = self.get_node_at(location)
            new.next = target.next
            if target == self.tail:
                self.tail = new
            target.next = new
        self.size += 1

    def pop(self):
        if self.is_empty:
            raise ValueError("List is empty")
        new_tail = self.get_node_at(self.size - 1)
        new_tail.next = None
        self.tail = new_tail
        self.size -= 1

    def remove(self, location: int):
        if self.is_empty:
            raise ValueError("List is empty")
        if self.size < location:
            raise ValueError("Invalid location")
        if self.size == 1:
            self.__init__()
            return

        target = self.head

        if location == 1:
            self.head = target.next
            return
        else:
            location -= 1
            while target.next and location - 1:
                target = target.next
                location -= 1
            target.next = target.next.next
        self.size -= 1

    def get_node_at(self, location: int) -> Node:
        if (location < 1) or self.size < location:
            raise ValueError("Invalid location")
        temp = self.head
        while (temp and temp.next) and location - 1:
            temp = temp.next
            location -= 1
        return temp

    def get_data_at(self, location: int):
        return self.get_node_at(location).data

    @property
    def is_empty(self):
        return True if not self.size else False
