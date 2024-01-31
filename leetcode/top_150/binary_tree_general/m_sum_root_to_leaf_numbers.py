from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode], total=0) -> int:
        total = total * 10 + root.val
        if root.left and root.right:
            return self.sumNumbers(root.left, total) + self.sumNumbers(root.right, total)
        elif root.left:
            return self.sumNumbers(root.left, total)
        elif root.right:
            return self.sumNumbers(root.right, total)
        return total


if __name__ == "__main__":
    inputs = [
        TreeNode(val=1, left=TreeNode(val=2), right=TreeNode(val=3)),
        TreeNode(
            val=4,
            left=TreeNode(val=9, left=TreeNode(val=5), right=TreeNode(val=1)),
            right=TreeNode(val=0, right=TreeNode(val=1)),
        ),
        TreeNode(val=1),
        TreeNode(
            val=1,
            right=TreeNode(
                val=2, right=TreeNode(val=3, right=TreeNode(val=4, right=TreeNode(val=5, right=TreeNode(val=6))))
            ),
        ),
    ]
    s = Solution()
    for root in inputs:
        print(s.sumNumbers(root))
