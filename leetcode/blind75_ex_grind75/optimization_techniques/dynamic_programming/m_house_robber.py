class Solution:
    def rob(self, nums: list[int]) -> int:
        nums = [0] + nums
        for i in range(2, len(nums)):
            nums[i] = max(nums[i] + nums[i - 2], nums[i - 1])
        return nums[-1]


class Solution2:
    def rob(self, nums: list[int]) -> int:
        rob1, rob2 = 0, 0
        for n in nums:
            rob1, rob2 = rob2, max(n + rob1, rob2)
        return rob2


class Solution3:
    def rob(self, nums: list[int]) -> int:
        stop = len(nums)
        if stop == 0:
            return 0
        memo = [0] * (stop + 1)
        memo[1] = nums[0]
        for i in range(1, stop):
            memo[i + 1] = max(nums[i] + memo[i - 1], memo[i])
        return memo[stop]


def main() -> None:
    inputs = [[1, 2, 3, 1], [2, 7, 9, 3, 1], [2], [1, 2], [2, 1, 1, 2]]
    s = Solution3()
    for nums in inputs:
        print(s.rob(nums))


if __name__ == "__main__":
    main()
