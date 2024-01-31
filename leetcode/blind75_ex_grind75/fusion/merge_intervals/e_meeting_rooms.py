from typing import List


class Solution:
    def meet(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return True
        intervals.sort(key=lambda i: i[0])
        prev = intervals[0]
        for i in range(1, len(intervals)):
            if prev[1] > intervals[i][0]:
                return False
            prev = intervals[i]
        return True


class Solution2:
    def meet(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i: i[0])
        for i in range(1, len(intervals)):
            if intervals[i - 1][1] > intervals[i][0]:
                return False
        return True


if __name__ == "__main__":
    inputs = [
        [[1, 2], [4, 6], [6, 8], [9, 12]],
        [[1, 5], [4, 6], [6, 8], [9, 12]],
        [[1, 10]],
        [[3, 10], [1, 15]],
        [],
    ]
    s = Solution()
    for intervals in inputs:
        print(s.meet(intervals))
