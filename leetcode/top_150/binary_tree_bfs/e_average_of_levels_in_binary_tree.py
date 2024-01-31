from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result = []
        queue = deque()
        queue.append(root)
        while queue:
            length = len(queue)
            num = 0
            for _ in range(length):
                node = queue.popleft()
                num += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(num / length)
        return result


if __name__ == "__main__":
    inputs = [
        TreeNode(val=3, left=TreeNode(val=9), right=TreeNode(val=20, left=TreeNode(val=15), right=TreeNode(val=7))),
        TreeNode(val=3, left=TreeNode(val=9, left=TreeNode(val=15), right=TreeNode(val=7)), right=TreeNode(val=20)),
    ]
    s = Solution()
    for root in inputs:
        print(s.averageOfLevels(root))
