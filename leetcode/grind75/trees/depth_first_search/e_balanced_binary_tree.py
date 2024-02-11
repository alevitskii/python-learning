from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def post_order(root):
            nonlocal balanced
            if root is None:
                return 0

            left_height = post_order(root.left)
            right_height = post_order(root.right)

            if abs(left_height - right_height) > 1:
                balanced = False

            return max(left_height, right_height) + 1

        balanced = True
        post_order(root)
        return balanced


class Solution2:
    def depth(self, root: TreeNode):
        if root is None:
            return 0
        left = self.depth(root.left)
        right = self.depth(root.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.depth(root) != -1


class Solution3:
    def isBalanced(self, root):
        def is_balanced_helper(node):
            if not node:
                return 0
            left = is_balanced_helper(node.left)
            if left == -1:
                return -1
            right = is_balanced_helper(node.right)
            if right == -1:
                return -1
            if abs(left - right) > 1:
                return -1
            return max(left, right) + 1

        return is_balanced_helper(root) != -1


def main() -> None:
    inputs = [
        TreeNode(2, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7))),
        TreeNode(
            1,
            left=TreeNode(2, left=TreeNode(3, left=TreeNode(4), right=TreeNode(4)), right=TreeNode(3)),
            right=TreeNode(2),
        ),
    ]

    s = Solution3()
    for root in inputs:
        print(s.isBalanced(root))


if __name__ == "__main__":
    main()
