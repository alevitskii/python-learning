from collections import defaultdict
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        current = intervals[0]
        result = []
        for i in range(1, len(intervals)):
            if current[1] >= intervals[i][0]:
                current[1] = max(intervals[i][1], current[1])
            else:
                result.append(current)
                current = intervals[i]
        return result + [current]


class Solution2:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # otherwise, there is overlap, so we merge the current and previous
                # intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged


# T: O(n**2), S: O(n**2)
class Solution3:
    def overlap(self, a, b):
        return a[0] <= b[1] and b[0] <= a[1]

    # generate graph where there is an undirected edge between intervals u
    # and v iff u and v overlap.
    def buildGraph(self, intervals):
        graph = defaultdict(list)

        for i, interval_i in enumerate(intervals):
            for j in range(i + 1, len(intervals)):
                if self.overlap(interval_i, intervals[j]):
                    graph[tuple(interval_i)].append(intervals[j])
                    graph[tuple(intervals[j])].append(interval_i)

        return graph

    # merges all of the nodes in this connected component into one interval.
    def mergeNodes(self, nodes):
        min_start = min(node[0] for node in nodes)
        max_end = max(node[1] for node in nodes)
        return [min_start, max_end]

    # gets the connected components of the interval overlap graph.
    def getComponents(self, graph, intervals):
        visited = set()
        comp_number = 0
        nodes_in_comp = defaultdict(list)

        def markComponentDFS(start):
            stack = [start]
            while stack:
                node = tuple(stack.pop())
                if node not in visited:
                    visited.add(node)
                    nodes_in_comp[comp_number].append(node)
                    stack.extend(graph[node])

        # mark all nodes in the same connected component with the same integer.
        for interval in intervals:
            if tuple(interval) not in visited:
                markComponentDFS(interval)
                comp_number += 1

        return nodes_in_comp, comp_number

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        graph = self.buildGraph(intervals)
        nodes_in_comp, number_of_comps = self.getComponents(graph, intervals)

        # all intervals in each connected component must be merged.
        return [self.mergeNodes(nodes_in_comp[comp]) for comp in range(number_of_comps)]


if __name__ == "__main__":
    inputs = [[[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 4], [4, 5]], [[1, 4]], [[1, 4], [5, 5]], [[1, 4], [0, 4]]]
    s = Solution()
    for intervals in inputs:
        print(s.merge(intervals))
