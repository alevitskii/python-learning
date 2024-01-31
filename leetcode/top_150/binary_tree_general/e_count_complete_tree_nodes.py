from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        pass


if __name__ == "__main__":
    inputs = [
        TreeNode(
            val=1,
            left=TreeNode(val=2, left=TreeNode(val=4), right=TreeNode(val=5)),
            right=TreeNode(val=3, left=TreeNode(val=6)),
        ),
    ]
    s = Solution()
    for root in inputs:
        print(s.countNodes(root))
