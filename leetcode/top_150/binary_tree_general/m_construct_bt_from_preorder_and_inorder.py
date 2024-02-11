from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not preorder:
            return None
        idx = inorder.index(preorder[0])
        root = TreeNode(
            val=preorder[0],
            left=self.buildTree(preorder[1 : idx + 1], inorder[:idx]),
            right=self.buildTree(preorder[idx + 1 :], inorder[idx + 1 :]),
        )
        return root


class Solution2:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        preorder_idx = 0

        def treeHelper(left, right):
            nonlocal preorder_idx
            if left > right:
                return None
            node_val = preorder[preorder_idx]
            root = TreeNode(node_val)
            preorder_idx += 1
            inorder_index = inorder_map[node_val]
            root.left = treeHelper(left, inorder_index - 1)
            root.right = treeHelper(inorder_index + 1, right)
            return root

        return treeHelper(0, len(inorder) - 1)


def main() -> None:
    inputs = [
        ([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]),
        ([-1], [-1]),
    ]
    s = Solution2()
    for preorder, inorder in inputs:
        root = s.buildTree(preorder, inorder)
        print(root)


if __name__ == "__main__":
    main()
