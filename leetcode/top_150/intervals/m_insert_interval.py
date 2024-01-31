from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        for i, interval in enumerate(intervals):
            if interval[1] < newInterval[0]:
                result.append(interval)
            elif interval[0] > newInterval[1]:
                return result + [newInterval] + intervals[i:]
            else:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])
        return result + [newInterval]


if __name__ == "__main__":
    inputs = [
        ([[1, 3], [6, 9]], [2, 5]),
        ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]),
        ([[3, 5]], [1, 8]),
        ([[1, 8]], [3, 5]),
        ([], [3, 5]),
        ([[1, 2], [3, 4], [5, 6]], [2, 5]),
        ([[2, 5], [6, 7], [8, 9]], [0, 1]),
        ([[2, 5], [6, 7], [8, 9]], [10, 11]),
    ]
    s = Solution()
    for intervals, newInterval in inputs:
        print(s.insert(intervals, newInterval))
