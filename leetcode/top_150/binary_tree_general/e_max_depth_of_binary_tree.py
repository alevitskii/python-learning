from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return max(self.maxDepth(root.left) + 1, self.maxDepth(root.right) + 1) if root else 0


if __name__ == "__main__":
    inputs = [
        TreeNode(val=3, left=TreeNode(val=9), right=TreeNode(val=20, left=TreeNode(15), right=TreeNode(7))),
    ]
    s = Solution()
    for head in inputs:
        print(s.maxDepth(head))
