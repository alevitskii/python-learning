from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def issym(leftsub, rightsub):
            if leftsub is None and rightsub is None:
                return True
            elif leftsub and rightsub and leftsub.val == rightsub.val:
                return issym(leftsub.left, rightsub.right) and issym(leftsub.right, rightsub.left)
            return False

        return issym(root.left, root.right)


if __name__ == "__main__":
    inputs = [
        TreeNode(
            val=1,
            left=TreeNode(val=2, left=TreeNode(val=3), right=TreeNode(val=4)),
            right=TreeNode(val=2, left=TreeNode(val=4), right=TreeNode(val=3)),
        ),
        TreeNode(val=1, left=TreeNode(val=2, right=TreeNode(val=3)), right=TreeNode(val=2, right=TreeNode(3))),
    ]
    s = Solution()
    for root in inputs:
        print(s.isSymmetric(root))
