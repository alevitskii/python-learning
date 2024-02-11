import heapq
import random
from typing import List


class SolutionQS:
    def distance(self, point):
        return point[0] ** 2 + point[1] ** 2

    def quick_select(self, points, left, right, k):
        pivot_point = points[right]
        index, pivot_index = left, left
        while index < right:
            if self.distance(points[index]) < self.distance(pivot_point):
                points[index], points[pivot_index] = points[pivot_index], points[index]
                pivot_index += 1
            index += 1
        points[pivot_index], points[right] = points[right], points[pivot_index]
        if pivot_index == k:
            return
        elif pivot_index < k:
            self.quick_select(points, pivot_index + 1, right, k)
        else:
            self.quick_select(points, left, pivot_index - 1, k)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points) == k:
            return points
        self.quick_select(points, 0, len(points) - 1, k)
        return points[:k]


class SolutionSort:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points, key=lambda x: (x[0] ** 2 + x[1] ** 2))[:k]


class SolutionHeap:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points) == k:
            return points
        heap = []
        for i in range(len(points) - k):
            x, y = points[i]
            heapq.heappush(heap, (x**2 + y**2, x, y))
        for i in range(len(points) - k, len(points)):
            x, y = points[i]
            if x**2 + y**2 > heap[0][0]:
                heapq.heapreplace(heap, (x**2 + y**2, x, y))
        largest = {(x, y) for _, x, y in heap}
        return [point for point in points if tuple(point) not in largest]


class SolutionHeap2:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points) == k:
            return points
        heap = []
        for i in range(k):
            x, y = points[i]
            heapq.heappush(heap, (-(x**2 + y**2), x, y))
        for i in range(k, len(points)):
            x, y = points[i]
            if -(x**2 + y**2) > heap[0][0]:
                heapq.heapreplace(heap, (-(x**2 + y**2), x, y))
        return [coord for _, *coord in heap]


def main() -> None:
    inputs = [
        ([[1, 3], [-2, 2]], 1),
        ([[3, 3], [5, -1], [-2, 4]], 2),
        ([[0, 1], [1, 0]], 2),
        (
            [
                [68, 97],
                [34, -84],
                [60, 100],
                [2, 31],
                [-27, -38],
                [-73, -74],
                [-55, -39],
                [62, 91],
                [62, 92],
                [-57, -67],
            ],
            5,
        ),
    ]
    s = SolutionHeap()
    for points, k in inputs:
        print(s.kClosest(points, k))


if __name__ == "__main__":
    main()
