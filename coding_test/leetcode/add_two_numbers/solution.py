# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        answer = None
        carry = False
        a = l1
        b = l2

        while a or b or carry:
            val1 = 0
            val2 = 0

            if a:
                val1 = a.val
                a = a.next

            if b:
                val2 = b.val
                b = b.next

            new_value = val1 + val2

            if carry:
                new_value += 1

            if 9 < new_value:
                carry = True
                new_value = new_value % 10
            else:
                carry = False

            if answer is None:
                answer = ListNode(new_value)
            else:
                temp = answer
                while temp.next is not None:
                    temp = temp.next
                temp.next = ListNode(new_value)

        return answer
