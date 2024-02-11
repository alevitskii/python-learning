class UnionFind:
    # Constructor
    def __init__(self, n):
        # List to store parent nodes
        self.parent = []
        # List to store ranks of subsets
        self.rank = [1] * (n + 1)

        # Initially setting each element as its own parent
        for i in range(n + 1):
            self.parent.append(i)

    # Function to find which subset a particular element belongs
    def find(self, v):
        if self.parent[v] != v:
            # Path compression
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    # Function to join two subsets into a single subset
    def union(self, x, y):
        # Find the representatives of the subsets
        p1, p2 = self.find(x), self.find(y)

        # Elements are already in the same subset
        if p1 == p2:
            return False
        # Set p1 as parent of p2
        elif self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            # Update rank of p1
            self.rank[p1] = self.rank[p1] + self.rank[p2]
        else:
            # Set p2 as parent of p1
            self.parent[p1] = p2
            # Update rank of p2
            self.rank[p2] = self.rank[p2] + self.rank[p1]

        return True


class Solution:
    def connected(self, n: int, edges: list[list[int]]) -> int:
        dsu = UnionFind(n)
        res = n
        for x, y in edges:
            if dsu.union(x, y):
                res -= 1
        return res


def main() -> None:
    inputs = [
        (5, [[0, 1], [1, 2], [3, 4]]),
        (8, [[0, 1], [1, 2], [4, 5], [6, 7]]),
        (10, [[0, 2], [2, 3], [4, 5], [5, 6], [7, 8], [8, 9]]),
    ]
    s = Solution()
    for n, edges in inputs:
        print(s.connected(n, edges))


if __name__ == "__main__":
    main()
