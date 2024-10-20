from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        head = dummy
        p1, p2 = list1, list2
        while head:
            if p1 and p2:
                if p1.val <= p2.val:
                    head.next = p1
                    p1 = p1.next
                else:
                    head.next = p2
                    p2 = p2.next
            elif p1:
                head.next = p1
                p1 = p1.next
            elif p2:
                head.next = p2
                p2 = p2.next
            head = head.next
        return dummy.next
