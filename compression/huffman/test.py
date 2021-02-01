import unittest

from .huffman import huffman_decode, huffman_encode


class TestCase(unittest.TestCase):
    def test_huffman(self) -> None:
        encoded, prefix_tree = huffman_encode("aaabbaaccdeaf")
        self.assertEqual(encoded, "00011111100101101110010001101")
        decoded = huffman_decode(encoded, prefix_tree)
        self.assertEqual(decoded, "aaabbaaccdeaf")

    def test_same_value_data(self) -> None:
        encoded, prefix_tree = huffman_encode("ppppppppppp")
        self.assertEqual(encoded, "00000000000")
        decoded = huffman_decode(encoded, prefix_tree)
        self.assertEqual(decoded, "ppppppppppp")
