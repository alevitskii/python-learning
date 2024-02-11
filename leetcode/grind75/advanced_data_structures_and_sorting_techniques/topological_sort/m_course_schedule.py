from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(course):
            if course in visited:
                return False
            if mapping[course] == []:
                return True
            visited.add(course)
            for pre in mapping[course]:
                if not dfs(pre):
                    return False
            visited.remove(course)
            mapping[course] = []
            return True

        mapping = {C: [] for C in range(numCourses)}
        for course, pre in prerequisites:
            mapping[course].append(pre)
        visited = set()
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True


class Solution2:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for main, prerequisite in prerequisites:
            graph[prerequisite].append(main)
            indegree[main] += 1
        stack = []
        for i in range(numCourses):
            if indegree[i] == 0:
                stack.append(i)
        count = 0
        while stack:
            current = stack.pop()
            count += 1
            for neighbour in graph[current]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    stack.append(neighbour)
        return count == numCourses


class Solution3:
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
