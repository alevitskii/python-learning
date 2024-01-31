from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        idx = inorder.index(postorder[-1])
        root = TreeNode(
            val=postorder[-1],
            left=self.buildTree(inorder[:idx], postorder[:idx]),
            right=self.buildTree(inorder[idx + 1 :], postorder[idx:-1]),
        )
        return root


class Solution2:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)
        idx_map = {val: idx for idx, val in enumerate(inorder)}

        def helper(left, right):
            if left > right:
                return None
            val = postorder.pop()
            root = TreeNode(val)
            index = idx_map[val]
            root.right = helper(index + 1, right)
            root.left = helper(left, index - 1)
            return root

        return helper(0, n - 1)


if __name__ == "__main__":
    inputs = [
        ([9, 3, 15, 20, 7], [9, 15, 7, 20, 3]),
        ([-1], [-1]),
    ]
    s = Solution()
    for inorder, postorder in inputs:
        root = s.buildTree(inorder, postorder)
        print(root)
