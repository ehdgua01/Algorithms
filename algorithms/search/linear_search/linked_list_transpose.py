class Node(object):
    def __init__(self, value) -> None:
        self.next = None
        self.value = value

    def __iter__(self):
        return NodeIterator(self)


class NodeIterator(object):
    def __init__(self, current: Node):
        self.current: Node = current

    def __iter__(self) -> Node:
        return self.current

    def __next__(self):
        if self.current:
            current = self.current
            self.current = current.next
            return current
        else:
            raise StopIteration


def linked_list_transpose(head: Node, match):
    prev = None
    pprev = None

    for node in head:
        if node.value == match:
            if prev:
                if pprev:
                    pprev.next = node
                prev.next = node.next
                node.next = prev
            return node

        if prev:
            pprev = prev
        prev = node
