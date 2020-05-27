"""
대용량의 데이터를 정렬하는데 부적합한 퀵 정렬을 개선
"""
from typing import List, Any


class Node(object):
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class Stack(object):
    def __init__(self) -> None:
        self.top = None
        self.size = 0

    def pop(self) -> Any:
        if self.is_empty:
            raise Exception("Stack is empty")
        data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return data

    def push(self, new: Node) -> None:
        if not isinstance(new, Node):
            raise TypeError("Not node type")
        if self.is_empty:
            self.top = new
        else:
            new.next = self.top
            self.top = new
        self.size += 1

    def peek(self) -> Any:
        return None if self.is_empty else self.top.data

    @property
    def is_empty(self) -> bool:
        return self.top is None


def partition(data: List[Any], left: int, right: int) -> int:
    lessor = index = left
    pivot = data[lessor]
    greater = right

    while index <= greater:
        if data[index] < pivot:
            data[index], data[lessor] = data[lessor], data[index]
            lessor += 1
            index += 1
        elif pivot < data[index]:
            data[index], data[greater] = data[greater], data[index]
            greater -= 1
        else:
            index += 1

    return lessor


def stack_quick_sort(data: List[Any]) -> List[Any]:
    lesser = 0
    greater = len(data) - 1
    s = Stack()
    s.push(Node((0, -1)))

    while not s.is_empty:
        while lesser <= greater:
            pivot = partition(data, lesser, greater)
            s.push(Node((pivot + 1, greater)))
            greater = pivot - 1
        lesser, greater = s.pop()
    return data
