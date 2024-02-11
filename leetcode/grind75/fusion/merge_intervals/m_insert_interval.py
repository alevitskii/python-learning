from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_intervals = []

        for n, i in enumerate(intervals):
            if i[0] > newInterval[1]:
                return new_intervals + [newInterval] + intervals[n:]
            elif i[1] < newInterval[0]:
                new_intervals.append(i)
            else:
                newInterval = [min(newInterval[0], i[0]), max(newInterval[1], i[1])]

        return new_intervals + [newInterval]


class Solution2:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_start, new_end = newInterval[0], newInterval[1]
        i = 0
        n = len(intervals)
        output = []
        while i < n and intervals[i][0] < new_start:
            output.append(intervals[i])
            i = i + 1
        if not output or output[-1][1] < new_start:
            output.append(newInterval)
        else:
            output[-1][1] = max(output[-1][1], new_end)
        while i < n:
            ei = intervals[i]
            start, end = ei[0], ei[1]
            if output[-1][1] < start:
                output.append(ei)
            else:
                output[-1][1] = max(output[-1][1], end)
            i += 1
        return output


def main() -> None:
    inputs = [
        ([[1, 3], [6, 9]], [2, 5]),
        ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]),
        ([[1, 5]], [2, 3]),
        ([[1, 5]], [6, 8]),
    ]

    s = Solution2()
    for intervals, new_interval in inputs:
        print(s.insert(intervals, new_interval))


if __name__ == "__main__":
    main()
