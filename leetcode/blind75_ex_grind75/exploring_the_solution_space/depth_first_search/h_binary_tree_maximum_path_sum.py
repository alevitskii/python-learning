from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            nonlocal max_val
            if node is None:
                return 0
            left_max_single_path = dfs(node.left)
            right_max_single_path = dfs(node.right)
            max_val = max(max_val, node.val + max(left_max_single_path, 0) + max(right_max_single_path, 0))
            return max(max(left_max_single_path, right_max_single_path) + node.val, node.val)

        max_val = float("-inf")
        dfs(root)
        return max_val


class Solution2:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0
            max_left = dfs(root.left)
            max_right = dfs(root.right)
            left_subtree = 0
            right_subtree = 0
            if max_left > 0:
                left_subtree = max_left
            if max_right > 0:
                right_subtree = max_right
            value_new_path = root.val + left_subtree + right_subtree
            max_sum = dfs.max_sum
            dfs.max_sum = max(max_sum, value_new_path)
            return root.val + max(left_subtree, right_subtree)

        dfs.max_sum = float("-inf")
        dfs(root)
        return dfs.max_sum


if __name__ == "__main__":
    inputs = [
        TreeNode(1, left=TreeNode(2), right=TreeNode(3)),
        TreeNode(-10, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7))),
        TreeNode(-3),
        TreeNode(
            1,
            left=TreeNode(-2, left=TreeNode(1, left=TreeNode(-1)), right=TreeNode(3)),
            right=TreeNode(-3, left=TreeNode(-2)),
        ),
    ]
    s = Solution()
    for root in inputs:
        print(s.maxPathSum(root))
