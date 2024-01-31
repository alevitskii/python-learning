from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: int, q: int) -> TreeNode:
        if not root or root.val == p or root.val == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left or right


if __name__ == "__main__":
    inputs = [
        (
            TreeNode(
                val=3,
                left=TreeNode(
                    val=5, left=TreeNode(val=6), right=TreeNode(val=2, left=TreeNode(val=7), right=TreeNode(val=4))
                ),
                right=TreeNode(val=1, left=TreeNode(val=0), right=TreeNode(val=8)),
            ),
            5,
            1,
        ),
        (
            TreeNode(
                val=3,
                left=TreeNode(
                    val=5, left=TreeNode(val=6), right=TreeNode(val=2, left=TreeNode(val=7), right=TreeNode(val=4))
                ),
                right=TreeNode(val=1, left=TreeNode(val=0), right=TreeNode(val=8)),
            ),
            5,
            4,
        ),
        (TreeNode(val=1, left=TreeNode(val=2)), 1, 2),
    ]
    s = Solution()
    for root, p, q in inputs:
        node = s.lowestCommonAncestor(root, p, q)
        print()
