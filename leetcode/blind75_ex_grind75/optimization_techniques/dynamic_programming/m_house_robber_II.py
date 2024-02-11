class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        rob1, rob2 = 0, 0
        for n in nums[1:]:
            rob1, rob2 = rob2, max(n + rob1, rob2)
        max_rob1 = rob2
        rob1, rob2 = 0, 0
        for n in nums[:-1]:
            rob1, rob2 = rob2, max(n + rob1, rob2)
        max_rob2 = rob2
        return max(max_rob1, max_rob2)


class Solution2:
    def rob(self, nums: list[int]) -> int:
        rob1_x1st, rob2_x1st = 0, 0
        rob1_xlast, rob2_xlast = 0, 0
        for i, n in enumerate(nums):
            if i != 0:
                rob1_x1st, rob2_x1st = rob2_x1st, max(n + rob1_x1st, rob2_x1st)
            if i != len(nums) - 1:
                rob1_xlast, rob2_xlast = rob2_xlast, max(n + rob1_xlast, rob2_xlast)
        return max(nums[0], rob2_x1st, rob2_xlast)


def main() -> None:
    inputs = [
        [2, 3, 2],
        [1, 2, 3, 1],
        [2, 7, 9, 3, 1],
        [2],
        [1, 2],
        [1, 2, 3],
    ]
    s = Solution2()
    for nums in inputs:
        print(s.rob(nums))


if __name__ == "__main__":
    main()
