from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.result = 0

    def findTilt(self, root: Optional[TreeNode]) -> int:
        def sum_subtree(subtree):
            if subtree is None:
                return 0
            left = sum_subtree(subtree.left)
            right = sum_subtree(subtree.right)
            self.result += abs(left - right)
            return subtree.val + left + right

        if root is None:
            return 0
        left_subtree_total = sum_subtree(root.left)
        right_subtree_total = sum_subtree(root.right)
        return self.result + abs(left_subtree_total - right_subtree_total)
