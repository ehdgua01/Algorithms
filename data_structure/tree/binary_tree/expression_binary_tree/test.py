import unittest

from .expression_binary_tree import (
    postfix_to_tree, calculate_expression_tree,
)


class TestCase(unittest.TestCase):
    def test_expression_1(self):
        expr = ['1', '2', '+', '3', '+']
        tree = postfix_to_tree(expr)
        self.assertEqual(tree.value, '+')
        self.assertEqual(tree.left.value, '+')
        self.assertEqual(tree.left.left.value, 1.0)
        self.assertEqual(tree.left.right.value, 2.0)
        self.assertEqual(tree.right.value, 3.0)
        self.assertEqual(calculate_expression_tree(tree), 6)

    def test_expression_2(self):
        expr = [
            '1', '2', '123', '*', '2323', '*', '999',
            '+', '123', '*', '+', '1', '+',
        ]
        tree = postfix_to_tree(expr)
        self.assertEqual(calculate_expression_tree(tree), 70412213)
