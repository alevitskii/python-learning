# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> int:
        if p is None and q is None:
            return True
        elif p is not None and q is not None and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False


def main() -> None:
    inputs = [
        (
            TreeNode(val=1, left=TreeNode(val=2), right=TreeNode(val=3)),
            TreeNode(val=1, left=TreeNode(val=2), right=TreeNode(val=3)),
        ),
        (
            TreeNode(val=1, left=TreeNode(val=2)),
            TreeNode(val=1, right=TreeNode(val=2)),
        ),
    ]
    s = Solution()
    for p, q in inputs:
        print(s.isSameTree(p, q))


if __name__ == "__main__":
    main()
