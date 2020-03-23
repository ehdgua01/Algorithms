import unittest

from .huffman import huffman_encode


class TestCase(unittest.TestCase):
    def test_huffman(self):
        encoded, prefix_tree = huffman_encode("abcdef")
