from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        arrows = 1
        intersection = points[0]
        for i in range(1, len(points)):
            point = points[i]
            if point[0] <= intersection[1]:
                intersection = [max(intersection[0], point[0]), min(intersection[1], point[1])]
            else:
                intersection = point
                arrows += 1
        return arrows


def main() -> None:
    inputs = [
        [[10, 16], [2, 8], [1, 6], [7, 12]],
        [[1, 2], [3, 4], [5, 6], [7, 8]],
        [[1, 2], [2, 3], [3, 4], [4, 5]],
        [[9, 12], [1, 10], [4, 11], [8, 12], [3, 9], [6, 9], [6, 7]],
    ]
    s = Solution()
    for points in inputs:
        print(s.findMinArrowShots(points))


if __name__ == "__main__":
    main()
