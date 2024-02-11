from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        def dfs(left, right):
            if left > right:
                return 0
            if (left, right) in dp:
                return dp[(left, right)]
            dp[(left, right)] = 0
            for i in range(left, right + 1):
                coins = nums[left - 1] * nums[i] * nums[right + 1] + dfs(left, i - 1) + dfs(i + 1, right)
                dp[(left, right)] = max(dp[(left, right)], coins)
            return dp[(left, right)]

        nums = [1] + nums + [1]
        dp = {}
        return dfs(1, len(nums) - 2)


def main() -> None:
    inputs = [
        [3, 1, 5, 8],
        [8, 3, 4, 3, 5, 0, 5, 6, 6, 2, 8, 5, 6, 2, 3, 8, 3, 5, 1, 0, 2, 9],
        [1, 5],
        [3, 1, 5],
    ]
    s = Solution()
    for nums in inputs:
        print(s.maxCoins(nums))


if __name__ == "__main__":
    main()
