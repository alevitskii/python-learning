from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1 if root else 0


class Solution2:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        nodes_stack = deque([(root, 1)])
        max_depth = 0
        while nodes_stack:
            node, depth = nodes_stack.pop()
            if node.left:
                nodes_stack.append((node.left, depth + 1))
            if node.right:
                nodes_stack.append((node.right, depth + 1))
            if not node.left and not node.right:
                max_depth = max(max_depth, depth)
        return max_depth


if __name__ == "__main__":
    inputs = [
        TreeNode(3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7))),
        TreeNode(1, right=TreeNode(2)),
    ]

    s = Solution2()
    for root in inputs:
        print(s.maxDepth(root))
