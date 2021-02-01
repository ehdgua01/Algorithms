import unittest

from .solution import ListNode, Solution


class TestCase(unittest.TestCase):
    def test_case_1(self) -> None:
        node1 = ListNode(2)
        node1.next = ListNode(4)
        node1.next.next = ListNode(3)

        node2 = ListNode(5)
        node2.next = ListNode(6)
        node2.next.next = ListNode(4)

        answer = Solution().addTwoNumbers(node1, node2)
        self.assertEqual(answer.val, 7)
        self.assertEqual(answer.next.val, 0)
        self.assertEqual(answer.next.next.val, 8)

    def test_case_2(self) -> None:
        node1 = ListNode(2)
        node1.next = ListNode(4)
        node1.next.next = ListNode(3)

        node2 = ListNode(5)
        node2.next = ListNode(6)
        node2.next.next = ListNode(6)

        answer = Solution().addTwoNumbers(node1, node2)
        self.assertEqual(answer.val, 7)
        self.assertEqual(answer.next.val, 0)
        self.assertEqual(answer.next.next.val, 0)
        self.assertEqual(answer.next.next.next.val, 1)
