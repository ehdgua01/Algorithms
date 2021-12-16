from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        self.it = self

    def __iter__(self):
        self.it = self
        return self

    def __next__(self):
        if self.it:
            try:
                return self.it
            finally:
                self.it = self.it.next
        raise StopIteration()


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, temp = head, ListNode()
        while curr:
            pos = temp
            while pos.next and pos.next.val < curr.val:
                pos = pos.next

            curr.next, pos.next, curr = pos.next, curr, curr.next
        return temp.next
