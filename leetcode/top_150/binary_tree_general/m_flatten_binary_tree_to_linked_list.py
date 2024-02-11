from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None
        if root.left is None and root.right is None:
            return root
        if root.left:
            node = self.flatten(root.left)
            node.right = root.right
            root.right = root.left
            root.left = None
            return self.flatten(node)
        else:
            return self.flatten(root.right)


class Solution2:
    def __init__(self) -> None:
        self.prev = None

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.flatten(root.right)  # Recursively flatten the right subtree
        self.flatten(root.left)  # Recursively flatten the left subtree
        root.right = self.prev  # Set the right child to the previously flattened node
        root.left = None  # Set the left child to None
        self.prev = root  # Update the previously flattened node to be the current node


def main() -> None:
    inputs = [
        TreeNode(
            val=1,
            left=TreeNode(val=2, left=TreeNode(val=3), right=TreeNode(val=4)),
            right=TreeNode(val=5, right=TreeNode(val=6)),
        ),
        TreeNode(
            val=1,
            right=TreeNode(
                val=2, right=TreeNode(val=3, right=TreeNode(val=4, right=TreeNode(val=5, right=TreeNode(val=6))))
            ),
        ),
        TreeNode(val=0),
        TreeNode(val=1, left=TreeNode(val=2, left=TreeNode(val=3))),
        None,
    ]
    s = Solution2()
    for root in inputs:
        s.flatten(root)
        print(root)


if __name__ == "__main__":
    main()
