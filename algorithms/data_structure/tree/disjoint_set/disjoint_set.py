from abc import ABC, abstractmethod


class AbstractDisjointSetNode(ABC):
    @abstractmethod
    def find_set(self):
        pass

    @abstractmethod
    def union(self, node):
        pass


class DisjointSetNode(AbstractDisjointSetNode):
    def __init__(self, value):
        self.parent = None
        self.value = value

    def find_set(self):
        if self.parent is None:
            return self

        temp = self.parent
        while temp.parent:
            temp = temp.parent
        return temp

    def union(self, node) -> None:
        node.parent = self.find_set()
