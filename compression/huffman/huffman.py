from typing import Tuple, Dict, Union
from collections import Counter


class Node(object):
    def __init__(self, value: Union[str, None], freq: int):
        self.value = value
        self.freq = freq
        self.bitstring: str = ""
        self.left: Union[Node, None] = None
        self.right: Union[Node, None] = None

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
    prefix_tree = None
    encoded = ""

    for k, v in sorted(freq.items(), key=lambda x: x[1]):
        if prefix_tree is None:
            prefix_tree = Node(k, v)
        else:
            parent = Node(None, prefix_tree.freq + v)
            parent.left = Node(k, v)
            parent.right = prefix_tree
            prefix_tree = parent

    prefix_table = create_prefix_table(prefix_tree)

    for c in string:
        encoded += prefix_table[c]

    return encoded, prefix_tree


def huffman_decode(encoded: str) -> str:
    decoded = encoded
    return decoded
