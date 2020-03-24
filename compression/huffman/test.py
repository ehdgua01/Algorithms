import unittest

from .huffman import huffman_encode, huffman_decode


class TestCase(unittest.TestCase):
    def test_huffman(self):
        encoded, prefix_tree = huffman_encode("aaabbaaccdeaf")
        self.assertEqual(encoded, "00011111100101101110010001101")
        decoded = huffman_decode(encoded, prefix_tree)
        self.assertEqual(decoded, "aaabbaaccdeaf")

        encoded, prefix_tree = huffman_encode("ppppppppppp")
        self.assertEqual(encoded, "00000000000")
        decoded = huffman_decode(encoded, prefix_tree)
        self.assertEqual(decoded, "ppppppppppp")
