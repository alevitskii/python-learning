from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(node):
            nonlocal k
            if node is None:
                return None
            left = inorder(node.left)
            if left:
                return left
            k -= 1
            if k == 0:
                return node
            return inorder(node.right)

        return inorder(root)


if __name__ == "__main__":
    inputs = [
        (TreeNode(val=3, left=TreeNode(val=1, right=TreeNode(val=2)), right=TreeNode(val=4)), 1),
        (
            TreeNode(
                val=5,
                left=TreeNode(val=3, left=TreeNode(val=2, left=TreeNode(val=1)), right=TreeNode(val=4)),
                right=TreeNode(val=6),
            ),
            3,
        ),
    ]
    s = Solution()
    for root, k in inputs:
        print(s.kthSmallest(root, k))
