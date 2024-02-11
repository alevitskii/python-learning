from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        from bisect import bisect_left

        result = [nums[0]]
        for n in nums:
            if n <= result[-1]:
                i = bisect_left(result, n)
                result[i] = n
            else:
                result.append(n)
        return len(result)


class Solution2:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        result = [1] * length
        for i in range(length - 1, -1, -1):
            for j in range(i + 1, length):
                if nums[i] < nums[j]:
                    result[i] = max(result[i], 1 + result[j])
        return max(result)


def main() -> None:
    inputs = [
        # [10, 9, 2, 5, 3, 7, 101, 18],
        # [0, 1, 0, 3, 2, 3],
        # [7, 0, 1, 0, 2],
        # [7, 7, 7, 7, 7, 7, 7],
        [1, 2, 3, 0, 2],
    ]
    s = Solution()
    for nums in inputs:
        print(s.lengthOfLIS(nums))


if __name__ == "__main__":
    main()
