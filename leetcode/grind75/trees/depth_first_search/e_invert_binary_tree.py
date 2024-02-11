from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        self.invertTree(root.right)
        self.invertTree(root.left)
        root.right, root.left = root.left, root.right
        return root


def main() -> None:
    inputs = [
        TreeNode(
            4,
            left=TreeNode(2, left=TreeNode(1), right=TreeNode(3)),
            right=TreeNode(7, left=TreeNode(6), right=TreeNode(9)),
        ),
        TreeNode(1, left=TreeNode(2), right=TreeNode(3)),
    ]

    s = Solution()
    for root in inputs:
        print(s.invertTree(root))


if __name__ == "__main__":
    main()
