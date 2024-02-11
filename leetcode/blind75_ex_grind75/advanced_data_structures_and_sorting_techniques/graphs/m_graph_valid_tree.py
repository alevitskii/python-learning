from collections import defaultdict


class Solution:
    def isValidTree(self, n: int, edges: list[list[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        adj_list = defaultdict(list)
        for p, nb in edges:
            adj_list[p].append(nb)
            adj_list[nb].append(p)
        stack = [0]
        seen = {0}
        while stack:
            node = stack.pop()
            for nb in adj_list[node]:
                if nb not in seen:
                    seen.add(nb)
                    stack.append(nb)
        return len(seen) == n


def main() -> None:
    inputs = [
        (5, [[0, 1], [0, 2], [0, 3], [3, 4]]),
        (5, [[0, 1], [0, 2], [0, 3], [0, 4], [3, 4]]),
        (3, [[0, 1], [0, 2], [1, 2]]),
    ]
    s = Solution()
    for n, edges in inputs:
        print(s.isValidTree(n, edges))


if __name__ == "__main__":
    main()
