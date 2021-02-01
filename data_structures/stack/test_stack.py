import unittest

from .stack import Node, Stack


class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.stack = Stack()

    def test_push(self):
        self.assertRaises(TypeError, self.stack.push, new=1)

        self.stack.push(Node(1))
        self.assertEqual(self.stack.size, 1)
        self.assertEqual(self.stack.top.data, 1)
        self.assertIsNone(self.stack.top.next)

        self.stack.push(Node(2))
        self.assertEqual(self.stack.size, 2)
        self.assertEqual(self.stack.top.data, 2)
        self.assertEqual(self.stack.top.next.data, 1)

        self.stack.push(Node(3))
        self.assertEqual(self.stack.size, 3)
        self.assertEqual(self.stack.top.data, 3)
        self.assertEqual(self.stack.top.next.data, 2)

    def test_is_empty(self):
        self.assertIs(self.stack.is_empty, True)
        self.stack.push(Node(1))
        self.assertIs(self.stack.is_empty, False)

    def test_peek(self):
        self.stack.push(Node(1))
        self.assertEqual(self.stack.peek(), 1)
        self.stack.push(Node(2))
        self.assertEqual(self.stack.peek(), 2)

    def test_get_size(self):
        self.stack.push(Node(1))
        self.assertEqual(self.stack.get_size(), 1)
        self.stack.push(Node(2))
        self.assertEqual(self.stack.get_size(), 2)

    def test_pop(self):
        self.assertRaises(Exception, self.stack.pop)
        for i in range(1, 11):
            self.stack.push(Node(i))
        self.assertEqual(self.stack.get_size(), 10)
        self.assertEqual(self.stack.pop(), 10)
        self.assertEqual(self.stack.peek(), 9)
        self.assertEqual(self.stack.get_size(), 9)
        self.assertEqual(self.stack.pop(), 9)
        self.assertEqual(self.stack.peek(), 8)
        self.assertEqual(self.stack.get_size(), 8)


if __name__ == "__main__":
    unittest.main()
