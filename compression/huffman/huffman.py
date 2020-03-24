from typing import Tuple, Dict, Union
from collections import Counter
from queue import PriorityQueue


class Node(object):
    def __init__(self, value: Union[str, None], bitstring=None, left=None, right=None):
        self.value = value
        self.bitstring: str = bitstring
        self.left: Union[Node, None] = left
        self.right: Union[Node, None] = right

    def __eq__(self, other):
        if other.value is None:
            return self
        elif self.value is None:
            return other
        else:
            if other.value < self.value:
                return self
            else:
                return other

    @property
    def is_identifier(self) -> bool:
        return self.value is not None

    @property
    def is_leaf(self) -> bool:
        return (self.left or self.right) is None


def create_prefix_table(prefix_tree: Node, bitstring="") -> Dict[str, str]:
    prefix_table = {}

    if prefix_tree.is_identifier:
        prefix_table[prefix_tree.value] = bitstring
    else:
        prefix_table.update(create_prefix_table(prefix_tree.left, bitstring + "0"))
        prefix_table.update(create_prefix_table(prefix_tree.right, bitstring + "1"))
    return prefix_table


def huffman_encode(string: str) -> Tuple[str, Node]:
    freq = Counter(string)
    encoded = ""
    priority_queue = PriorityQueue()

    for k, v in freq.items():
        priority_queue.put((v, Node(k)))

    while True:
        if priority_queue.qsize() == 1:
            prefix_tree = priority_queue.get()[1]
            break

        left = priority_queue.get()
        right = priority_queue.get()
        parent = Node(None, left=left[1], right=right[1])
        priority_queue.put((left[0] + right[0], parent))

    if prefix_tree.is_identifier:
        prefix_table = {prefix_tree.value: "0"}
    else:
        prefix_table = create_prefix_table(prefix_tree)

    for c in string:
        encoded += prefix_table[c]

    return encoded, prefix_tree


def huffman_decode(encoded: str, prefix_tree: Node) -> str:
    decoded = ""
    temp = prefix_tree

    if temp.is_leaf:
        return temp.value * len(encoded)

    for c in encoded:
        if c == "1":
            temp = temp.right
        else:
            temp = temp.left

        if temp.is_leaf:
            decoded += temp.value
            temp = prefix_tree
    return decoded
