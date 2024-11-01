# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-101)
        left, right, prev_value = dummy, head, dummy.val
        while right and right.next:
            if right.val != prev_value and right.val != right.next.val:
                left.next = ListNode(right.val)
                left = left.next
            prev_value = right.val
            right = right.next
        if right and right.val != prev_value:
            left.next = ListNode(right.val)
        return dummy.next
