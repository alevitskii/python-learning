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


class Solution3:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build_tree_helper(p_order, i_order, left, right, mapping, p_index):
            if left > right:
                return None
            curr = p_order[p_index[0]]
            p_index[0] += 1
            root = TreeNode(curr)
            if left == right:
                return root
            in_index = mapping[curr]
            root.left = build_tree_helper(p_order, i_order, left, in_index - 1, mapping, p_index)
            root.right = build_tree_helper(p_order, i_order, in_index + 1, right, mapping, p_index)
            return root

        p_index = [0]
        mapping = {}
        for i in range(len(preorder)):
            mapping[inorder[i]] = i
        return build_tree_helper(preorder, inorder, 0, len(preorder) - 1, mapping, p_index)


if __name__ == "__main__":
    inputs = [
        # ([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]),
        # ([-1], [-1]),
        ([3, 2, 3, 4], [3, 2, 3, 4])
    ]
    s = Solution()
    for preorder, inorder in inputs:
        root = s.buildTree(preorder, inorder)
        print(root)
