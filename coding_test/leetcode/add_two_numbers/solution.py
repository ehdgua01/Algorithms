# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry, new_value = divmod(l1.val + l2.val + 0, 10)
        answer = ListNode(new_value)
        tail = answer

        while l1.next or l2.next or carry:
            a = l1.next.val if l1.next else 0
            b = l2.next.val if l2.next else 0
            carry, new_value = divmod(a + b + carry, 10)

            tail.next = ListNode(new_value)
            tail = tail.next

            l1 = l1.next if l1.next else l1
            l2 = l2.next if l2.next else l2
        return answer
