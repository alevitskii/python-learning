from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionPreOrder:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(root):
            if root is None:
                return
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)

        invert(root)
        return root


class SolutionPostOrder:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return
        self.invertTree(root.right)
        self.invertTree(root.left)
        root.right, root.left = root.left, root.right
        return root


if __name__ == "__main__":
    inputs = [
        TreeNode(
            val=4,
            left=TreeNode(val=2, left=TreeNode(val=1), right=TreeNode(val=3)),
            right=TreeNode(val=7, left=TreeNode(val=6), right=TreeNode(val=9)),
        ),
        TreeNode(val=2, left=TreeNode(val=1), right=TreeNode(val=3)),
    ]
    s = SolutionPostOrder()
    for root in inputs:
        print(s.invertTree(root))
