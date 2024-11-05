from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.is_leaf = left is right is None


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        stack = []

        def backtrack(node: TreeNode):
            stack.append(node.val)

            if node.is_leaf:
                result.append("->".join(map(str, stack)))
                return

            if node.left:
                backtrack(node.left)
                stack.pop()
            if node.right:
                backtrack(node.right)
                stack.pop()

        backtrack(root)
        return result


def test_binary_tree_paths():
    s = Solution()
    assert s.binaryTreePaths(TreeNode(1)) == ["1"]
    assert s.binaryTreePaths(
        TreeNode(
            1,
            left=TreeNode(
                2,
                right=TreeNode(5),
            ),
            right=TreeNode(3),
        )
    ) == ["1->2->5", "1->3"]
