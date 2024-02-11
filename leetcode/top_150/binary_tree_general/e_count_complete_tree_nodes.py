from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left, right = root, root
        left_height, right_height = 0, 0
        while left:
            left_height += 1
            left = left.left
        while right:
            right_height += 1
            right = right.right
        if left_height == right_height:  # Root is a complete tree
            return pow(2, left_height) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)


def main() -> None:
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


if __name__ == "__main__":
    main()
