from typing import List


# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def elements_equal(self, grid):
        control = [grid[0][0]] * len(grid)
        return grid[0][0] if all(i == control for i in grid) else None

    def split(self, grid):
        mid = len(grid) // 2
        topleft, topright, bottomleft, bottomright = [], [], [], []
        for i in range(mid):
            topleft.append(grid[i][:mid])
            topright.append(grid[i][mid:])
            bottomleft.append(grid[mid + i][:mid])
            bottomright.append(grid[mid + i][mid:])
        return topleft, topright, bottomleft, bottomright

    def construct(self, grid: List[List[int]]) -> Node:
        val = self.elements_equal(grid)
        node = Node(val=val, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None)
        if val is not None:
            node.val = val
            node.isLeaf = True
            return node
        topleft, topright, bottomleft, bottomright = self.split(grid)
        node.topLeft = self.construct(topleft)
        node.topRight = self.construct(topright)
        node.bottomLeft = self.construct(bottomleft)
        node.bottomRight = self.construct(bottomright)
        return node


def main() -> None:
    inputs = [
        # [[0, 1],
        #  [1, 0]],
        # [[1, 1, 1, 1, 0, 0, 0, 0],
        #  [1, 1, 1, 1, 0, 0, 0, 0],
        #  [1, 1, 1, 1, 1, 1, 1, 1],
        #  [1, 1, 1, 1, 1, 1, 1, 1],
        #  [1, 1, 1, 1, 0, 0, 0, 0],
        #  [1, 1, 1, 1, 0, 0, 0, 0],
        #  [1, 1, 1, 1, 0, 0, 0, 0],
        #  [1, 1, 1, 1, 0, 0, 0, 0]],
        [
            [1, 1, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 1, 1],
            [1, 1, 0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 0, 0, 1, 1],
            [1, 1, 1, 1, 1, 1, 0, 0],
            [1, 1, 1, 1, 1, 1, 0, 0],
        ]
    ]
    s = Solution()
    for grid in inputs:
        root = s.construct(grid)
        print(root)


if __name__ == "__main__":
    main()
