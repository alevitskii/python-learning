from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = {v: 0 for v in range(numCourses)}
        adj_list = defaultdict(list)
        for main, pre in prerequisites:
            indegree[main] += 1
            adj_list[pre].append(main)
        stack = [v for v in indegree if not indegree[v]]
        while stack and numCourses:
            v = stack.pop()
            for neighbor in adj_list[v]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    stack.append(neighbor)
            numCourses -= 1
        return stack == [] and numCourses == 0


def main() -> None:
    inputs = [
        ([[1, 0]], 2),
        ([[1, 0], [0, 1]], 2),
    ]
    s = Solution()
    for prerequisites, numCourses in inputs:
        print(s.canFinish(numCourses, prerequisites))


if __name__ == "__main__":
    main()
