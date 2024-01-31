import heapq
from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        queue = deque()
        queue.append(root)
        heap = []
        while queue:
            node = queue.popleft()
            heapq.heappush(heap, node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return heapq.nsmallest(k, heap)[-1]


class Solution2:
    def kthSmallest(self, root, k):
        self.count = 0
        self.result = 0
        self.inorderTraversal(root, k)
        return self.result

    def inorderTraversal(self, node, k):
        if not node or self.count >= k:
            return
        self.inorderTraversal(node.left, k)
        self.count += 1
        if self.count == k:
            self.result = node.val
            return
        self.inorderTraversal(node.right, k)


if __name__ == "__main__":
    inputs = [
        (TreeNode(val=3, left=TreeNode(val=1, right=TreeNode(val=2)), right=TreeNode(val=4)), 1),
        (
            TreeNode(
                val=5,
                left=TreeNode(val=3, left=TreeNode(val=2, left=TreeNode(val=1)), right=TreeNode(val=4)),
                right=TreeNode(val=6),
            ),
            3,
        ),
    ]
    s = Solution2()
    for root, k in inputs:
        print(s.kthSmallest(root, k))
