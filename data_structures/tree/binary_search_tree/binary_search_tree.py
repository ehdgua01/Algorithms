"""
대용량의 데이터에 적합하지 않은 알고리즘이지만,
이진 탐색 트리 자료 구조를 학습하기 위한 알고리즘입니다.
"""


class Node(object):
    def __init__(self, value) -> None:
        self.left = None
        self.right = None
        self.parent = None
        self.value = value


class BinarySearchTree(object):
    def __init__(self) -> None:
        self.root = None

    def get_min(self, collection: Node, /) -> Node:
        if collection.left:
            return self.get_min(collection.left)
        else:
            return collection

    def get_max(self, collection: Node, /) -> Node:
        if collection.right:
            return self.get_max(collection.right)
        else:
            return collection

    def find_index(self, target: Node, /, collection=None):
        if self.is_empty or collection is None:
            return None
        else:
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
            return self.find_index(target, collection=collection,)

    def insert(self, node: Node, /) -> None:
        if self.is_empty:
            self.root = node
        else:
            index = self.find_index(node, collection=self.root,)
            node.parent = index
            if index.value < node.value:
                index.right = node
            else:
                index.left = node

    def search(self, target, /, collection=None):
        if self.is_empty or collection is None:
            return None
        else:
            if collection.value == target:
                return collection
            elif collection.value < target:
                return self.search(target, collection=collection.right,)
            else:
                return self.search(target, collection=collection.left,)

    def remove(self, target, /):
        if self.is_empty:
            return None

        collection = self.search(target, collection=self.root,)

        if collection is None:
            return None
        else:
            self.__remove(collection, collection.parent)

    def __remove(self, collection: Node, parent, /):
        temp = None
        if collection.right and collection.left:
            temp = self.get_min(collection.right)
            self.__remove(temp, temp.parent)
            temp.left = collection.left
            temp.right = collection.right
        elif collection.right:
            temp = collection.right
        elif collection.left:
            temp = collection.left

        if temp:
            temp.parent = parent

        if parent:
            is_left = parent.left == collection
            if is_left:
                parent.left = temp
            else:
                parent.right = temp
        else:
            self.root = temp

    @property
    def is_empty(self):
        return self.root is None
