import heapq
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        heap = []
        heapq.heappush(heap, -intervals[0][1])
        for i in range(1, len(intervals)):
            if intervals[i][0] < -heap[0]:
                if intervals[i][1] < -heap[0]:
                    heapq.heapreplace(heap, -intervals[i][1])
            else:
                heapq.heappush(heap, -intervals[i][1])
        return len(intervals) - len(heap)


class Solution2:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        end = float("-inf")
        remove = 0
        for interval in intervals:
            if interval[0] >= end:
                end = interval[1]
            else:
                remove += 1
        return remove


if __name__ == "__main__":
    inputs = [
        # [[1, 2], [2, 3], [3, 4], [1, 3]],
        # [[1, 2], [1, 2], [1, 2]],
        # [[1, 2], [2, 3]],
        # [[1, 2], [2, 4], [3, 6], [5, 10]],
        # [[1, 5], [1, 5], [2, 8], [7, 9], [10, 12]],
        [[3, 5], [5, 10], [10, 15], [12, 13], [14, 20], [21, 23], [23, 25], [25, 27]],
        [[4, 8], [8, 14], [15, 17], [16, 17]],
        [[10, 20], [20, 30], [30, 40], [40, 50], [50, 60]],
    ]
    s = Solution2()
    for intervals in inputs:
        print(s.eraseOverlapIntervals(intervals))
