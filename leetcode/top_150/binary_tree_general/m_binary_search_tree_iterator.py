from collections import deque
from typing import Generator, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.iterator = self._inorder(self.root)
        self.max_element = self._get_max(self.root)
        self.has_next = True

    def _get_max(self, root):
        while root.right:
            root = root.right
        return root.val

    def _inorder(self, root):
        if root.left:
            yield from self._inorder(root.left)
        self.has_next = root.val != self.max_element
        yield root.val
        if root.right:
            yield from self._inorder(root.right)

    def next(self) -> int:
        return next(self.iterator)

    def hasNext(self) -> bool:
        return self.has_next


class BSTIterator2:
    def __init__(self, root: Optional[TreeNode]):
        self.iter = self._inorder(root)
        self.nxt = next(self.iter, None)

    def _inorder(self, node: Optional[TreeNode]) -> Generator[int, None, None]:
        if node:
            yield from self._inorder(node.left)
            yield node.val
            yield from self._inorder(node.right)

    def next(self) -> int:
        res, self.nxt = self.nxt, next(self.iter, None)
        return res

    def hasNext(self) -> bool:
        return self.nxt is not None


def main() -> None:
    root = TreeNode(val=7, left=TreeNode(val=3), right=TreeNode(val=15, left=TreeNode(val=9), right=TreeNode(val=20)))
    bSTIterator = BSTIterator(root)
    print(bSTIterator.next())  # return 3
    print(bSTIterator.next())  # return 7
    print(bSTIterator.hasNext())  # return True
    print(bSTIterator.next())  # return 9
    print(bSTIterator.hasNext())  # return True
    print(bSTIterator.next())  # return 15
    print(bSTIterator.hasNext())  # return True
    print(bSTIterator.next())  # return 20
    print(bSTIterator.hasNext())  # return False


if __name__ == "__main__":
    main()
