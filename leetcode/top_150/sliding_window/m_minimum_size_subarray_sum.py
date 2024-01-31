from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 1
        min_length = float("inf")
        acc = nums[0]
        while True:
            if acc >= target:
                min_length = min(min_length, right - left)
                acc -= nums[left]
                left += 1
            else:
                if right >= len(nums):
                    break
                acc += nums[right]
                right += 1
        return min_length if min_length != float("inf") else 0


class Solution2:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        def subarray_exists(length: int):
            s = sum(nums[:length])
            if target <= s:
                return True
            for i in range(length, len(nums)):
                s -= nums[i - length]
                s += nums[i]
                if target <= s:
                    return True

            return False

        lst, r = 1, len(nums)

        while lst <= r:
            m = (lst + r) // 2
            if subarray_exists(length=m):
                r = m - 1
            else:
                lst = m + 1
        return 0 if lst > len(nums) else lst


if __name__ == "__main__":
    inputs = [
        (7, [2, 3, 1, 2, 4, 3]),
        (1, [1, 4, 4]),
        (11, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),
        (1, [1, 1, 1]),
        (213, [12, 28, 83, 4, 25, 26, 25, 2, 25, 25, 25, 12]),
    ]
    s = Solution2()
    for target, nums in inputs:
        print(s.minSubArrayLen(target, nums))
