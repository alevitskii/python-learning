# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root


class Solution2:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        while True:
            if root.val < min(p.val, q.val):
                root = root.right
            elif root.val > max(p.val, q.val):
                root = root.left
            else:
                return root


class Solution3:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        if root.val == p.val:
            return p
        elif root.val == q.val:
            return q
        elif root.val < max(p.val, q.val) and root.val > min(p.val, q.val):
            return root
        return self.lowestCommonAncestor(root.left, p, q) or self.lowestCommonAncestor(root.right, p, q)


if __name__ == "__main__":
    inputs = [
        (
            TreeNode(
                6,
                left=TreeNode(2, left=TreeNode(0), right=TreeNode(4, left=TreeNode(3), right=TreeNode(5))),
                right=TreeNode(8, left=TreeNode(7), right=TreeNode(9)),
            ),
            TreeNode(2),
            TreeNode(8),
        ),
        (
            TreeNode(
                6,
                left=TreeNode(2, left=TreeNode(0), right=TreeNode(4, left=TreeNode(3), right=TreeNode(5))),
                right=TreeNode(8, left=TreeNode(7), right=TreeNode(9)),
            ),
            TreeNode(2),
            TreeNode(4),
        ),
        (TreeNode(2, left=TreeNode(1)), TreeNode(2), TreeNode(1)),
    ]
    s = Solution()
    for root, p, q in inputs:
        print(s.lowestCommonAncestor(root, p, q))
