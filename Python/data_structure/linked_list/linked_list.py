class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.pointer = None
        self.size = 0

    def clear(self):
        self.__init__()

    def is_empty(self):
        return True if not self.size else False

    def append(self, node: Node):
        if self.is_empty():
            self.head = node
            self.pointer = self.head
        else:
            self.tail = self.head
            while self.tail.next_node is not None:
                self.tail = self.tail.next_node
            self.tail.next_node = node
            self.tail = node

        print('데이터 추가 완료')
        self.size += 1

    def insert(self, node: Node):
        if self.is_empty():
            self.head = node
            self.pointer = self.head
        else:
            if self.pointer.next_node is None:
                self.tail = node
            node.next_node = self.pointer.next_node
            self.pointer.next_node = node

        print('데이터 삽입 완료')
        self.size += 1

    def pop(self):
        if self.is_empty():
            return None

        if not self.tail:
            self.head = None
            self.pointer = None

        tail = None
        remove = self.head

        while remove.next_node is not None:
            tail = remove
            remove = remove.next_node

        tail.next_node = None

        if remove == self.pointer:
            self.pointer = tail
        self.tail = tail
        self.size -= 1

    def next(self):
        if self.is_empty():
            return None

        if not self.pointer.next_node:
            print('다음 노드가 존재하지 않습니다.')
        else:
            self.pointer = self.pointer.next_node
            return self.pointer.data

    def move_to_head(self):
        if self.is_empty():
            return None

        self.pointer = self.head
        print('포인터를 첫 번째 노드로 이동했습니다.')

    def move_to_tail(self):
        if self.is_empty():
            return None

        self.pointer = self.tail
        print("포인터를 마지막 노드로 이동했습니다.")

    def get_head(self):
        return self.head.data if self.head else None

    def get_current(self):
        return self.pointer.data if self.pointer else None

    def get_tail(self):
        return self.tail.data if self.tail else None

    def get_size(self):
        return self.size


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert(Node("Insert1"))
    linked_list.append(Node("test1"))
    linked_list.insert(Node("Insert2"))

    linked_list.move_to_tail()
    linked_list.append(Node("test2"))
    linked_list.insert(Node("Insert3"))
    linked_list.pop()

    linked_list.move_to_head()
    print(linked_list.get_current())
    while linked_list.next():
        print(linked_list.get_current())
