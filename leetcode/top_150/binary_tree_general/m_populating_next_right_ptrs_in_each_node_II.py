from collections import deque
from typing import List, Optional


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: "Node" = None, right: "Node" = None, next: "Node" = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        if root is None:
            return None
        queue = deque()
        queue.appendleft(root)
        while queue:
            length = len(queue)
            cnt = 0
            prev = None
            while cnt < length:
                node = queue.pop()
                node.next = prev
                prev = node
                if node.right:
                    queue.appendleft(node.right)
                if node.left:
                    queue.appendleft(node.left)
                cnt += 1
        return root


if __name__ == "__main__":
    inputs = [Node(val=1, left=Node(val=2, left=Node(4), right=Node(5)), right=Node(val=3, right=Node(7))), None]
    s = Solution()
    for root in inputs:
        root = s.connect(root)
        print(root)
