class Node(object):
    def __init__(self, value: int) -> None:
        self.prev = None
        self.next = None
        self.value = value

    def __iter__(self):
        return NodeIterator(self)

    def insert(self, node) -> None:
        if self.next:
            node.next = self.next
            self.next.prev = node
        else:
            node.next = None
        self.next = node
        node.prev = self

    def pop(self):
        if self.next:
            self.next.prev = self.prev
        if self.prev:
            self.prev.next = self.next
        return self


class NodeIterator(object):
    def __init__(self, node: Node):
        self.current: Node = node

    def __iter__(self) -> Node:
        return self.current

    def __next__(self) -> Node:
        if self.current:
            current = self.current
            self.current = self.current.next
            return current
        else:
            raise StopIteration


def linked_list_i_sort(data: Node) -> Node:
    if data.next is None:
        return data

    i = data
    while i:
        if (i.prev is None) or (i.prev.value <= i.value):
            i = i.next
            continue
        for j in data:
            if i.value < j.value:
                j.prev.insert(i.pop())
                break
        i = i.next
