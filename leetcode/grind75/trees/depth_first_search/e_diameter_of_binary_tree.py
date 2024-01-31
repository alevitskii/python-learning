# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(root):
            nonlocal diameter
            if root is None:
                return 0
            left_height = dfs(root.left)
            right_height = dfs(root.right)
            diameter = max(diameter, left_height + right_height)
            return max(left_height, right_height) + 1

        diameter = 0
        dfs(root)
        return diameter


if __name__ == "__main__":
    inputs = [
        TreeNode(1, left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)), right=TreeNode(3)),
        TreeNode(1, left=TreeNode(2)),
        TreeNode(1, left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)), right=TreeNode(3, left=TreeNode(6))),
    ]

    s = Solution()
    for root in inputs:
        print(s.diameterOfBinaryTree(root))
