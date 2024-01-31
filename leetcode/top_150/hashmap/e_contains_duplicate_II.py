from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        s = set()
        k = min(k, len(nums) - 1)
        for i in range(k):
            if nums[i] in s:
                return True
            s.add(nums[i])
        left, right = 0, k
        while right < len(nums):
            if nums[right] in s:
                return True
            s.discard(nums[left])
            s.add(nums[right])
            left += 1
            right += 1
        return False


class Solution2:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for i, n in enumerate(nums):
            if n in d and abs(d[n] - i) <= k:
                return True
            d[n] = i
        return False


if __name__ == "__main__":
    inputs = [
        ([1, 2, 3, 1], 3),
        ([1, 0, 1, 1], 1),
        ([1, 2, 3, 1, 2, 3], 2),
        ([1, 1], 2),
        ([1, 2, 2, 3], 3),
        ([1, 2, 2, 3], 0),
    ]
    s = Solution()
    for nums, k in inputs:
        print(s.containsNearbyDuplicate(nums, k))
