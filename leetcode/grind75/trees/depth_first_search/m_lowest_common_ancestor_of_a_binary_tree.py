# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: int, q: int) -> TreeNode:
        if not root or root.val == p or root.val == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left or right


class Solution2:
    def lowestCommonAncestor(self, root: TreeNode, p: int, q: int) -> TreeNode:
        def lowest_common_ancestor_rec(current_node, p, q):
            nonlocal lca
            if not current_node:
                return False
            left, right, mid = False, False, False
            if p == current_node.val or q == current_node.val:
                mid = True
            left = lowest_common_ancestor_rec(current_node.left, p, q)
            if not lca:
                right = lowest_common_ancestor_rec(current_node.right, p, q)
            if mid + left + right >= 2:
                lca = current_node
            return mid or left or right

        lca = None
        lowest_common_ancestor_rec(root, p, q)
        return lca


if __name__ == "__main__":
    inputs = [
        (
            TreeNode(
                val=3,
                left=TreeNode(
                    val=5, left=TreeNode(val=6), right=TreeNode(val=2, left=TreeNode(val=7), right=TreeNode(val=4))
                ),
                right=TreeNode(val=1, left=TreeNode(val=0), right=TreeNode(val=8)),
            ),
            5,
            1,
        ),
        (
            TreeNode(
                val=3,
                left=TreeNode(
                    val=5, left=TreeNode(val=6), right=TreeNode(val=2, left=TreeNode(val=7), right=TreeNode(val=4))
                ),
                right=TreeNode(val=1, left=TreeNode(val=0), right=TreeNode(val=8)),
            ),
            5,
            4,
        ),
        (TreeNode(val=1, left=TreeNode(val=2)), 1, 2),
    ]
    s = Solution2()
    for root, p, q in inputs:
        node = s.lowestCommonAncestor(root, p, q)
        print(node.val)
