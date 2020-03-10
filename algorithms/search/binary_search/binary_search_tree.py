class Node(object):
    def __init__(self, value) -> None:
        self.left = None
        self.right = None
        self.value = value


class BinarySearchTree(object):
    def __init__(self) -> None:
        self.root = None

    def insert(self, node: Node) -> None:
        if self.is_empty:
            self.root = node
        else:
            index = self.find_index(node)

            if index.value < node.value:
                index.right = node
            else:
                index.left = node

    def find_index(self, x: Node, /, root=None):
        if self.is_empty:
            return None
        else:
            if root is None:
                root = self.root

            if root.value < x.value:
                if root.right:
                    root = root.right
                else:
                    return root
            else:
                if root.left:
                    root = root.left
                else:
                    return root
            return self.find_index(x, root)

    @property
    def is_empty(self):
        return True if self.root is None else False
