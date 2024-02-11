import heapq
import random
from typing import List


class Solution0:
    def partition(self, array, left, right):
        pivot_index = random.randint(left, right)
        pivot_element = array[pivot_index]
        array[pivot_index], array[right] = array[right], array[pivot_index]
        partition_index = left
        for j in range(left, right):
            if array[j] < pivot_element:
                array[partition_index], array[j] = array[j], array[partition_index]
                partition_index += 1
        array[partition_index], array[right] = array[right], array[partition_index]
        return partition_index

    def quick_select(self, array, left, right, index_to_find):
        if left < right:
            partition_index = self.partition(array, left, right)
            if index_to_find == partition_index:
                return array[partition_index]
            elif index_to_find < partition_index:
                return self.quick_select(array, left, partition_index - 1, index_to_find)
            else:
                return self.quick_select(array, partition_index + 1, right, index_to_find)
        elif left == right:
            return array[left]

    # T: O(n**2), Θ(n), S: O(1) - with tail recursion, O(n)? - without
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return nums[0]
        index_to_find = len(nums) - k
        return self.quick_select(nums, 0, len(nums) - 1, index_to_find)


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        for n in nums[k:]:
            if n > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, n)
        return heap[0]


def main() -> None:
    inputs = [([3, 2, 1, 5, 6, 4], 2), ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)]
    s = Solution0()
    for nums, k in inputs:
        print(s.findKthLargest(nums, k))


if __name__ == "__main__":
    main()
