from collections import defaultdict
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = {v: 0 for v in range(numCourses)}
        adj_list = defaultdict(list)
        for main, pre in prerequisites:
            indegree[main] += 1
            adj_list[pre].append(main)
        stack = [v for v in indegree if not indegree[v]]
        result = []
        while stack and numCourses:
            v = stack.pop()
            result.append(v)
            for neighbor in adj_list[v]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    stack.append(neighbor)
            numCourses -= 1
        return result if (stack == [] and numCourses == 0) else []


def main() -> None:
    inputs = [
        ([[1, 0]], 2),
        ([[1, 0], [2, 0], [3, 1], [3, 2]], 4),
        ([], 1),
        ([[1, 0], [0, 1]], 2),
    ]
    s = Solution()
    for prerequisites, numCourses in inputs:
        print(s.findOrder(numCourses, prerequisites))


if __name__ == "__main__":
    main()
