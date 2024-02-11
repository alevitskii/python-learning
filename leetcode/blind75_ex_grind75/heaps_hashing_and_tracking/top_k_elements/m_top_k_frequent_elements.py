import heapq
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        f = defaultdict(int)
        for n in nums:
            f[n] += 1
        heap = []
        for n, f in f.items():
            if len(heap) < k:
                heapq.heappush(heap, (f, n))
                continue
            if f > heap[0][0]:
                heapq.heapreplace(heap, (f, n))
        return [n for _, n in heap]


class Solution2:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        f = defaultdict(int)
        for n in nums:
            f[n] += 1
        heap = []
        for n, f in f.items():
            heapq.heappush(heap, (f, n))
            if len(heap) > k:
                heapq.heappop(heap)
        return [n for _, n in heap]


def main() -> None:
    inputs = [([1, 1, 1, 2, 2, 3], 2), ([1], 1), ([5, 3, 1, 1, 1, 3, 5, 73, 1], 3)]
    s = Solution2()
    for nums, k in inputs:
        print(s.topKFrequent(nums, k))


if __name__ == "__main__":
    main()
