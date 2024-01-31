from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None
        if root.left is None and root.right is None:
            return root
        if root.left:
            node = self.flatten(root.left)
            node.right = root.right
            root.right = root.left
            root.left = None
            return self.flatten(node)
        else:
            return self.flatten(root.right)


if __name__ == "__main__":
    inputs = [
        TreeNode(
            val=1,
            left=TreeNode(val=2, left=TreeNode(val=3), right=TreeNode(val=4)),
            right=TreeNode(val=5, right=TreeNode(val=6)),
        ),
        TreeNode(
            val=1,
            right=TreeNode(
                val=2, right=TreeNode(val=3, right=TreeNode(val=4, right=TreeNode(val=5, right=TreeNode(val=6))))
            ),
        ),
        TreeNode(val=0),
        TreeNode(val=1, left=TreeNode(val=2, left=TreeNode(val=3))),
        None,
    ]
    s = Solution()
    for root in inputs:
        s.flatten(root)
        print(root)
