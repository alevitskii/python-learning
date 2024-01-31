from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        queue = deque([root]) if root else None
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels.append(level)
        return levels


class Solution2:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(root, depth=0):
            if not root:
                return
            if len(res) <= depth:
                res.append([root.val])
            else:
                res[depth].append(root.val)
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)
            return res

        res = []
        dfs(root)
        return res


class Solution3:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def level_order(root_: Optional[TreeNode]) -> tuple[TreeNode]:
            level = () if root_ is None else (root_,)
            while level:
                yield level
                level = tuple(child for node in level for child in (node.left, node.right) if child)

        return [[node.val for node in level] for level in level_order(root)]


if __name__ == "__main__":
    inputs = [
        TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))),
        TreeNode(1),
        None,
        TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, right=TreeNode(5))),
    ]
    s = Solution()
    for root in inputs:
        print(s.levelOrder(root))
