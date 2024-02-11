class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        prev, maxs = nums[0], nums[0]
        for i in nums[1:]:
            prev = max(i + prev, i)
            maxs = max(maxs, prev)
        return maxs


def main() -> None:
    inputs = [
        [-2, 1, -3, 4, -1, 2, 1, -5, 4],
        [1],
        [5, 4, -1, 7, 8],
    ]
    s = Solution()
    for nums in inputs:
        print(s.maxSubArray(nums))


if __name__ == "__main__":
    main()
