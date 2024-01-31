from collections import defaultdict, deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        result = []
        queue = deque()
        queue.append(root)
        reverse = False
        while queue:
            count, length = 0, len(queue)
            level = []
            while count < length:
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                count += 1
            if reverse:
                level.reverse()
            result.append(level)
            reverse = not reverse
        return result


class Solution2:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = defaultdict(list)
        queue = deque([(root, 0)])
        while queue:
            node, depth = queue.popleft()
            if depth % 2 == 0:
                ans[depth].append(node.val)
            else:
                ans[depth].insert(0, node.val)
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
        return ans.values()


if __name__ == "__main__":
    inputs = [
        TreeNode(val=3, left=TreeNode(val=9), right=TreeNode(val=20, left=TreeNode(val=15), right=TreeNode(val=7))),
        TreeNode(val=1, left=TreeNode(val=2, left=TreeNode(val=4)), right=TreeNode(val=3, right=TreeNode(val=5))),
        TreeNode(val=1),
        None,
    ]
    s = Solution2()
    for root in inputs:
        print(s.zigzagLevelOrder(root))
