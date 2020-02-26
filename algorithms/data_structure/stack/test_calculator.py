import unittest

from calculator import infix_to_postfix, calculate_postfix


class TestCase(unittest.TestCase):
    def test_infix_to_postfix(self):
        self.assertEqual(
            infix_to_postfix('1 + 2 + 3'),
            ['1', '2', '+', '3', '+'],
        )

        self.assertEqual(
            infix_to_postfix('1 + ( 2 * 123 * 2323 + 999 ) * 123 + 1'),
            ['1', '2', '123', '*', '2323', '*', '999', '+', '123', '*', '+', '1', '+'],
        )

    def test_calculate_postfix(self):
        postfix1 = infix_to_postfix('1 + 2 + 3')
        self.assertEqual(calculate_postfix(postfix1), 6)

        postfix2 = infix_to_postfix('1 + ( 2 * 123 * 2323 + 999 ) * 123 + 1')
        self.assertEqual(calculate_postfix(postfix2), 70412213)


if __name__ == '__main__':
    unittest.main()
