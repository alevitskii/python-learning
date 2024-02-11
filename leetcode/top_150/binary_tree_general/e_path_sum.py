from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None and targetSum - root.val == 0:
            return True
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)


def main() -> None:
    inputs = [
        (
            TreeNode(
                val=5,
                left=TreeNode(val=4, left=TreeNode(val=11, left=TreeNode(val=7), right=TreeNode(val=2))),
                right=TreeNode(val=8, left=TreeNode(val=13), right=TreeNode(val=4, right=TreeNode(1))),
            ),
            22,
        ),
        (TreeNode(val=1, left=TreeNode(val=2), right=TreeNode(val=3)), 5),
        (None, 0),
        (TreeNode(val=1, left=TreeNode(val=2)), 1),
    ]
    s = Solution()
    for root, targetSum in inputs:
        print(s.hasPathSum(root, targetSum))


if __name__ == "__main__":
    main()
