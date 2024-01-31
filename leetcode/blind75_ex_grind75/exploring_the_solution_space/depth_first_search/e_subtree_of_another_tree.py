from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def identical(self, root, subRoot):
        if not root and not subRoot:
            return True
        elif not root or not subRoot:
            return False
        return (
            root.val == subRoot.val
            and self.identical(root.left, subRoot.left)
            and self.identical(root.right, subRoot.right)
        )

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if self.identical(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


if __name__ == "__main__":
    inputs = [
        (
            TreeNode(val=3, left=TreeNode(val=4, left=TreeNode(1), right=TreeNode(2)), right=TreeNode(val=5)),
            TreeNode(val=4, left=TreeNode(val=1), right=TreeNode(val=2)),
        ),
        (
            TreeNode(
                val=3,
                left=TreeNode(val=4, left=TreeNode(1), right=TreeNode(2, left=TreeNode(0))),
                right=TreeNode(val=5),
            ),
            TreeNode(val=4, left=TreeNode(val=1), right=TreeNode(val=2)),
        ),
        (
            TreeNode(
                val=3,
                left=TreeNode(val=4, left=TreeNode(1), right=TreeNode(4, left=TreeNode(1), right=TreeNode(2))),
                right=TreeNode(val=5),
            ),
            TreeNode(val=4, left=TreeNode(val=1), right=TreeNode(val=2)),
        ),
        (
            TreeNode(val=3, left=TreeNode(val=4, left=TreeNode(1)), right=TreeNode(val=5, left=TreeNode(2))),
            TreeNode(val=3, left=TreeNode(val=1), right=TreeNode(val=2)),
        ),
    ]
    s = Solution()
    for root, subRoot in inputs:
        print(s.isSubtree(root, subRoot))
