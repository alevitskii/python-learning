from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def construct(nums, left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(val=nums[mid])
            node.left = construct(nums, left, mid - 1)
            node.right = construct(nums, mid + 1, right)
            return node

        return construct(nums, 0, len(nums) - 1)


if __name__ == "__main__":
    inputs = [[-10, -3, 0, 5, 9], [1, 3]]
    s = Solution()
    for nums in inputs:
        root = s.sortedArrayToBST(nums)
        print(root)
