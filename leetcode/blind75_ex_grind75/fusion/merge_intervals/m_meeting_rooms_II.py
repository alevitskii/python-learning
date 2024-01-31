import heapq
from typing import List


class Solution:
    def meet(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda i: i[0])
        heap = []
        heapq.heappush(heap, intervals[0][1])
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start >= heap[0]:
                heapq.heapreplace(heap, end)
            else:
                heapq.heappush(heap, end)
        return len(heap)


class Solution2:
    def meet(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[0])
        end_times_heap = []
        heapq.heappush(end_times_heap, intervals[0][1])
        for i in range(1, len(intervals)):
            if intervals[i][0] >= end_times_heap[0]:
                heapq.heappop(end_times_heap)
            heapq.heappush(end_times_heap, intervals[i][1])
        return len(end_times_heap)


if __name__ == "__main__":
    inputs = [
        # [[10, 50], [20, 100], [40, 60], [60, 91], [70, 95], [90, 120]],
        [[2, 8], [3, 4], [3, 9], [5, 11], [8, 20], [11, 15]],
        # [[1, 2], [4, 6], [6, 8], [9, 12]],
        # [[1, 10]],
        # [[3, 10], [1, 15]],
        # [],
    ]
    s = Solution()
    for intervals in inputs:
        print(s.meet(intervals))
