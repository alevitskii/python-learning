from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]
        adj = [set() for i in range(n)]
        for v1, v2 in edges:
            adj[v1].add(v2)
            adj[v2].add(v1)
        leaves = [i for i in range(n) if len(adj[i]) == 1]
        rem_nodes = n
        while rem_nodes > 2:
            rem_nodes -= len(leaves)
            temp_leaves = []
            while leaves:
                leaf = leaves.pop()
                neighbor = adj[leaf].pop()
                adj[neighbor].remove(leaf)
                if len(adj[neighbor]) == 1:
                    temp_leaves.append(neighbor)
            leaves = temp_leaves
        return leaves


def main() -> None:
    inputs = [
        (2, [[0, 1]]),
        (1, []),
        (3, [[0, 1], [1, 2]]),
        (4, [[1, 0], [1, 2], [2, 3]]),
        (6, [[0, 1], [0, 2], [0, 3], [0, 4], [4, 5]]),
    ]

    s = Solution()
    for n, edges in inputs:
        print(s.findMinHeightTrees(n, edges))


if __name__ == "__main__":
    main()
