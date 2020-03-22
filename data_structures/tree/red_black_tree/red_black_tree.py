class Node(object):
    def __init__(self, value) -> None:
        self.left = None
        self.right = None
        self.parent = None
        self.color = 0
        self.value = value

    @property
    def is_black(self):
        return self.color == 0

    @property
    def is_red(self):
        return self.color == 1

    @property
    def is_root(self):
        return self.parent is None

    @property
    def is_left(self):
        return self == self.parent.left

    @property
    def is_right(self):
        return self == self.parent.right

    @property
    def grandparent(self):
        return self.parent.parent

    @property
    def sibling(self):
        if self.is_left:
            return self.parent.right
        else:
            return self.parent.left


class RedBlackTree(object):
    empty_node = Node(None)

    def __init__(self):
        self.root = None

    def right_rotate(self, collection: Node):
        left = collection.left
        collection.left = left.right

        if collection.left != RedBlackTree.empty_node:
            collection.left.parent = collection

        left.parent = collection.parent

        if collection.is_root:
            self.root = left
        else:
            if collection.is_left:
                collection.parent.left = left
            else:
                collection.parent.right = left

        left.right = collection
        collection.parent = left

    def left_rotate(self, collection: Node):
        right = collection.right
        collection.right = right.left

        if right.left != RedBlackTree.empty_node:
            collection.right.parent = collection

        right.parent = collection.parent

        if collection.is_root:
            self.root = right
        else:
            if collection.is_right:
                collection.parent.right = right
            else:
                collection.parent.left = right

        right.left = collection
        collection.parent = right

    def get_min(self, collection: Node):
        while True:
            if collection.left == RedBlackTree.empty_node:
                return collection
            else:
                collection = collection.left

    def find_parent(self, target):
        if self.is_empty:
            return

        collection = self.root
        while True:
            if collection.value < target:
                if collection.right != RedBlackTree.empty_node:
                    collection = collection.right
                else:
                    break
            else:
                if collection.left != RedBlackTree.empty_node:
                    collection = collection.left
                else:
                    break
        return collection

    def search(self, target):
        if self.is_empty:
            return

        collection = self.root
        while collection != RedBlackTree.empty_node:
            if collection.value == target:
                return collection
            elif collection.value < target:
                collection = collection.right
            else:
                collection = collection.left

    def insert(self, value):
        x = Node(value)
        x.left = RedBlackTree.empty_node
        x.right = RedBlackTree.empty_node

        if self.is_empty:
            self.root = x
        elif parent := self.find_parent(value):
            x.parent = parent
            x.color = 1

            if x.parent.value < value:
                x.parent.right = x
            else:
                x.parent.left = x

            while not x.is_root and x.parent.is_red:
                if x.parent.is_left:
                    if x.parent.sibling.is_red:
                        x.parent.sibling.color = 0
                        x.parent.color = 0
                        x.grandparent.color = 1
                        x = x.grandparent
                    else:
                        if x.is_right:
                            x = x.parent
                            self.left_rotate(x)
                        x.parent.color = 0
                        x.grandparent.color = 1
                        self.right_rotate(x.grandparent)
                else:
                    if x.parent.sibling.is_red:
                        x.parent.sibling.color = 0
                        x.parent.color = 0
                        x.grandparent.color = 1
                        x = x.grandparent
                    else:
                        if x.is_left:
                            x = x.parent
                            self.right_rotate(x)
                        x.parent.color = 0
                        x.grandparent.color = 1
                        self.left_rotate(x.grandparent)
            self.root.color = 0

    def remove(self, target):
        if target := self.search(target):
            if (
                target.left == RedBlackTree.empty_node
                or target.right == RedBlackTree.empty_node
            ):
                removed = target
            else:
                removed = self.get_min(target)
                target.value = removed.value

            if removed.left != RedBlackTree.empty_node:
                successor = removed.left
            else:
                successor = removed.right

            successor.parent = removed.parent

            if removed.is_root:
                self.root = successor
            else:
                if removed.is_left:
                    removed.parent.left = successor
                else:
                    removed.parent.right = successor

            if removed.is_black:
                while not successor.is_root and successor.is_black:
                    if successor.sibling.is_red:
                        successor.sibling.color = 0
                        successor.parent.color = 1
                        self.left_rotate(successor.parent)
                    else:
                        if (
                            successor.sibling.left.is_black
                            and successor.sibling.right.is_black
                        ):
                            successor.sibling.color = 1
                            successor = successor.parent
                        else:
                            if successor.sibling.left.is_red:
                                successor.sibling.color = 1
                                successor.sibling.left.color = 0
                                self.right_rotate(successor.sibling)
                            successor.sibling.color = successor.parent.color
                            successor.parent.color = 0
                            successor.sibling.right.color = 0
                            self.left_rotate(successor.parent)
                            successor = self.root
                self.root.color = 0
            return removed

    @property
    def is_empty(self):
        return self.root is None or self.root == RedBlackTree.empty_node
