from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def traverse_pre_order(node, current_level):
            if node is None:
                return
            if current_level >= len(result):
                result.append(node.val)
            if node.right:
                traverse_pre_order(node.right, current_level + 1)
            if node.left:
                traverse_pre_order(node.left, current_level + 1)

        traverse_pre_order(root, 0)
        return result


def main() -> None:
    inputs = [
        TreeNode(val=1, left=TreeNode(val=2, right=TreeNode(val=5)), right=TreeNode(val=3, right=TreeNode(val=4))),
        TreeNode(val=1, right=TreeNode(val=3)),
        None,
    ]
    s = Solution()
    for root in inputs:
        print(s.rightSideView(root))


if __name__ == "__main__":
    main()
