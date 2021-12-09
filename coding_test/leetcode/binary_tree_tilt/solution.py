from typing import Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.result = 0

    def findTilt(self, root: Optional[TreeNode]) -> int:
        def traverse_subtree(subtree: Optional[TreeNode]) -> Tuple[int, int]:
            if subtree is None:
                return 0, 0

            left_total, left_tilt = traverse_subtree(subtree.left)
            right_total, right_tilt = traverse_subtree(subtree.right)
            self.result += left_tilt + right_tilt
            return (subtree.val + left_total + right_total), abs(
                left_total - right_total
            )

        if root is None:
            return 0
        _, tilt = traverse_subtree(root)
        self.result += tilt
        return self.result
