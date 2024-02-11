from math import inf
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, minv, maxv):
            if node is None:
                return True
            if minv < node.val < maxv:
                return validate(node.left, minv, node.val) and validate(node.right, node.val, maxv)
            return False

        return validate(root, -inf, inf)


def main() -> None:
    inputs = [
        TreeNode(2, left=TreeNode(1), right=TreeNode(3)),
        TreeNode(5, left=TreeNode(1), right=TreeNode(4, left=TreeNode(3), right=TreeNode(6))),
        TreeNode(1),
    ]
    s = Solution()
    for root in inputs:
        print(s.isValidBST(root))


if __name__ == "__main__":
    main()
