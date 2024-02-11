from heapq import heappop, heappush
from typing import List


# T: O(min(k⋅logk,m⋅n⋅log(m⋅n))), S: O(min(k,m⋅n))
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m, n = len(nums1), len(nums2)
        result, seen = [], set()
        minHeap = [(nums1[0] + nums2[0], (0, 0))]
        seen.add((0, 0))
        while k > 0 and minHeap:
            _, (i, j) = heappop(minHeap)
            result.append([nums1[i], nums2[j]])
            if i + 1 < m and (i + 1, j) not in seen:
                heappush(minHeap, (nums1[i + 1] + nums2[j], (i + 1, j)))
                seen.add((i + 1, j))
            if j + 1 < n and (i, j + 1) not in seen:
                heappush(minHeap, (nums1[i] + nums2[j + 1], (i, j + 1)))
                seen.add((i, j + 1))
            k -= 1
        return result


def main() -> None:
    inputs = [([1, 7, 11], [2, 4, 6], 3), ([1, 1, 2], [1, 2, 3], 2), ([1, 2], [3], 3)]
    s = Solution()
    for nums1, nums2, k in inputs:
        print(s.kSmallestPairs(nums1, nums2, k))


if __name__ == "__main__":
    main()
