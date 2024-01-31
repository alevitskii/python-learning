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
        def inorder(root):
            nonlocal k
            if root is None:
                return
            if kth_smallest := inorder(root.left):
                return kth_smallest
            if (k := k - 1) == 0:
                return root
            if kth_smallest := inorder(root.right):
                return kth_smallest

        return inorder(root).val


class Solution2:
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


if __name__ == "__main__":
    inputs = [
        (TreeNode(3, left=TreeNode(1, right=TreeNode(2)), right=TreeNode(4)), 1),
        (TreeNode(5, left=TreeNode(3, left=TreeNode(2, left=TreeNode(1)), right=TreeNode(4)), right=TreeNode(6)), 3),
    ]
    s = Solution()
    for root, k in inputs:
        print(s.kthSmallest(root, k))
