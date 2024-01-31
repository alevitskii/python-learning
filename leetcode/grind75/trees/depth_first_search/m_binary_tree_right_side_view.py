from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# T: O(n), S: O(n) (Θ(h) - height of the tree)
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def traverse_pre_order(node, current_level):
            if node is None:
                return
            if current_level >= len(result):
                result.append(node.val)
            if node.right:
                traverse_pre_order(node.right, current_level + 1)
            if node.left:
                traverse_pre_order(node.left, current_level + 1)

        result = []
        traverse_pre_order(root, 0)
        return result


# T: O(n), S: O(n) (Θ(w) - width)
class Solution2:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        queue = [root]
        result = []
        while queue:
            length, count = len(queue), 0
            while count < length:
                node = queue.pop(0)
                count += 1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(node.val)
        return result


class Solution3:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node, level, rside):
            if level == len(rside):
                rside.append(node.val)
            for child in [node.right, node.left]:
                if child:
                    dfs(child, level + 1, rside)

        if root is None:
            return []
        rside = []
        dfs(root, 0, rside)
        return rside


if __name__ == "__main__":
    inputs = [
        TreeNode(
            1,
            left=TreeNode(2, left=TreeNode(4, right=TreeNode(7, left=TreeNode(8))), right=TreeNode(5)),
            right=TreeNode(3, right=TreeNode(6)),
        ),
        TreeNode(1),
        None,
    ]

    s = Solution3()
    for root in inputs:
        print(s.rightSideView(root))
