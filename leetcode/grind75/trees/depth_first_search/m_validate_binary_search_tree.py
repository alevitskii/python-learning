import math
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = []

        def inorder(root):
            if root is None:
                return None
            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)

        inorder(root)
        return True if arr == list(sorted(set(arr))) else False


class Solution2:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        low, high = -math.inf, math.inf

        def isValidbst(root, low, high):
            if not root:
                return True
            if low <= root.val <= high:
                left_sub_tree = isValidbst(root.left, low, root.val - 1)
                right_sub_tree = isValidbst(root.right, root.val + 1, high)
                return left_sub_tree and right_sub_tree
            return False

        return isValidbst(root, low, high)


class Solution3:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate_bst_helper(root, prev):
            if not root:
                return True
            if not validate_bst_helper(root.left, prev):
                return False
            if root.val <= prev[0]:
                return False
            prev[0] = root.val
            return validate_bst_helper(root.right, prev)

        prev = [-math.inf]
        return validate_bst_helper(root, prev)


if __name__ == "__main__":
    inputs = [
        TreeNode(val=2, left=TreeNode(val=1), right=TreeNode(val=3)),
        TreeNode(val=5, left=TreeNode(val=1), right=TreeNode(val=4, left=TreeNode(3), right=TreeNode(6))),
    ]
    s = Solution3()
    for root in inputs:
        print(s.isValidBST(root))
