class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.size = [1] * n

    def find(self, v):
        if self.parent[v] != v:
            # Path compression
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union_by_size(self, x, y):
        p1, p2 = self.find(x), self.find(y)
        if p1 == p2:
            return
        if self.size[p1] > self.size[p2]:
            self.parent[p2] = p1
            self.size[p1] += self.size[p2]
        else:
            self.parent[p1] = p2
            self.size[p2] += self.size[p1]

    def union_by_rank(self, x, y):
        p1, p2 = self.find(x), self.find(y)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        else:
            self.parent[p2] = p1
            self.rank[p1] += 1
        return True


def connected(n: int, edges: list[list[int]]) -> int:
    dsu = UnionFind(n)
    res = n
    for x, y in edges:
        if dsu.union_by_rank(x, y):
            res -= 1
    return res


def longestConsecutive(nums: list[int]) -> int:
    if not nums:
        return 0
    uf = UnionFind(len(nums))
    hash_map = {v: i for i, v in enumerate(nums)}
    for n in nums:
        if n - 1 in hash_map:
            uf.union_by_size(hash_map[n - 1], hash_map[n])
        if n + 1 in hash_map:
            uf.union_by_size(hash_map[n + 1], hash_map[n])
    return max(uf.size)


def main() -> None:
    inputs1 = [
        (5, [[0, 1], [1, 2], [3, 4]]),
        (8, [[0, 1], [1, 2], [4, 5], [6, 7]]),
        (10, [[0, 2], [2, 3], [4, 5], [5, 6], [7, 8], [8, 9]]),
    ]
    for n, edges in inputs1:
        print(connected(n, edges))
    print()
    inputs2 = [[100, 4, 200, 1, 3, 2], [0, 3, 7, 2, 5, 8, 4, 6, 0, 1], [78, 2, 32, 4, 1, 3], [], [1, 2]]
    for nums in inputs2:
        print(longestConsecutive(nums))


if __name__ == "__main__":
    main()
