import unittest

from infix_to_postfix import infix_to_postfix


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


if __name__ == '__main__':
    unittest.main()
