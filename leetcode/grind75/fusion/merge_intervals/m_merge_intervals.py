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
        if not intervals:
            return None
        result = []
        result.append(intervals[0])
        for i in range(1, len(intervals)):
            prev_end = result[-1][1]
            cur_start, cur_end = intervals[i]
            if cur_start <= prev_end:
                result[-1][1] = max(cur_end, prev_end)
            else:
                result.append([cur_start, cur_end])
        return result


if __name__ == "__main__":
    inputs = [
        [[1, 3], [2, 6], [8, 10], [15, 18]],
        [[1, 4], [4, 5]],
    ]

    s = Solution2()
    for intervals in inputs:
        print(s.merge(intervals))
