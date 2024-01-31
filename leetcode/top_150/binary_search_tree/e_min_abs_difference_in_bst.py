from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev = float("-inf")
        min_diff = float("inf")

        def inorder(root):
            nonlocal prev, min_diff
            if not root:
                return
            if root.left:
                inorder(root.left)
            if root.val - prev < min_diff:
                min_diff = root.val - prev
            prev = root.val
            if root.right:
                inorder(root.right)

        inorder(root)
        return min_diff


if __name__ == "__main__":
    inputs = [
        TreeNode(val=4, left=TreeNode(val=2, left=TreeNode(val=1), right=TreeNode(val=3)), right=TreeNode(val=6)),
        TreeNode(val=1, left=TreeNode(val=0), right=TreeNode(val=48, left=TreeNode(val=12), right=TreeNode(val=49))),
        TreeNode(
            val=236, left=TreeNode(val=104, right=TreeNode(val=227)), right=TreeNode(val=701, right=TreeNode(val=911))
        ),
    ]
    s = Solution()
    for root in inputs:
        print(s.getMinimumDifference(root))
