from .solution import Solution, TreeNode


def test_solution():
    range_sum_bst = Solution().rangeSumBST
    assert (
        range_sum_bst(
            root=TreeNode(
                val=10,
                left=TreeNode(
                    val=5,
                    left=TreeNode(val=3),
                    right=TreeNode(val=7),
                ),
                right=TreeNode(
                    val=15,
                    right=TreeNode(val=18),
                ),
            ),
            low=7,
            high=15,
        )
        == 32
    )
    assert (
        range_sum_bst(
            root=TreeNode(
                val=10,
                left=TreeNode(
                    val=5,
                    left=TreeNode(
                        val=3,
                        left=TreeNode(val=1),
                    ),
                    right=TreeNode(
                        val=7,
                        left=TreeNode(val=6),
                    ),
                ),
                right=TreeNode(
                    val=15,
                    left=TreeNode(val=13),
                    right=TreeNode(val=18),
                ),
            ),
            low=6,
            high=10,
        )
        == 23
    )
