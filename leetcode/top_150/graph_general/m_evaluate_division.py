from collections import defaultdict
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def find(adj_list, current, to_find, seen, path=1):
            if current in seen:
                return
            if current == to_find:
                return path
            seen.add(current)
            for v in adj_list[current]:
                res = find(adj_list, v[0], to_find, seen, path * v[1])
                if res is not None:
                    return res

        adj_list = defaultdict(list)
        for i, eq in enumerate(equations):
            adj_list[eq[0]].append((eq[1], values[i]))
            adj_list[eq[1]].append((eq[0], 1 / values[i]))
        result = []
        for q in queries:
            if q[0] not in adj_list or q[1] not in adj_list:
                result.append(-1.0)
            elif q[0] == q[1]:
                result.append(1.0)
            else:
                res = find(adj_list, q[0], q[1], set())
                result.append(res if res is not None else -1)
        return result


def main() -> None:
    inputs = [
        ([["a", "b"], ["b", "c"]], [2.0, 3.0], [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]),
        ([["a", "b"], ["b", "c"], ["bc", "cd"]], [1.5, 2.5, 5.0], [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]),
        ([["a", "b"]], [0.5], [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]),
        (
            [["x1", "x2"], ["x2", "x3"], ["x3", "x4"], ["x4", "x5"]],
            [3.0, 4.0, 5.0, 6.0],
            [["x1", "x5"], ["x5", "x2"], ["x2", "x4"], ["x2", "x2"], ["x2", "x9"], ["x9", "x9"]],
        ),
        ([["a", "b"], ["c", "d"]], [1.0, 1.0], [["a", "c"], ["b", "d"], ["b", "a"], ["d", "c"]]),
    ]
    s = Solution()
    for equations, values, queries in inputs:
        print(s.calcEquation(equations, values, queries))


if __name__ == "__main__":
    main()
