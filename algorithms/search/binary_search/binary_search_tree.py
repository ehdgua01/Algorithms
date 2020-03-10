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
            index = self.find_index(node, collection=self.root)

            if index.value < node.value:
                index.right = node
            else:
                index.left = node

    def search(self, target, /, collection=None):
        if self.is_empty:
            return None
        else:
            if collection is None:
                return None

            if collection.value == target:
                return collection.value
            elif collection.value < target:
                return self.search(target, collection=collection.right)
            else:
                return self.search(target, collection=collection.left)

    def find_index(self, target: Node, /, collection=None):
        if self.is_empty:
            return None
        else:
            if collection is None:
                return None

            if collection.value < target.value:
                if collection.right:
                    collection = collection.right
                else:
                    return collection
            else:
                if collection.left:
                    collection = collection.left
                else:
                    return collection
            return self.find_index(target, collection=collection)

    @property
    def is_empty(self):
        return True if self.root is None else False
