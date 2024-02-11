class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res = max(nums)
        cur_min, cur_max = 1, 1
        for n in nums:
            temp = cur_max * n
            cur_max = max(cur_max * n, n * cur_min, n)
            cur_min = min(temp, n * cur_min, n)
            res = max(res, cur_max)
        return res


class Solution2:
    def maxProduct(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far
        for i in range(1, len(nums)):
            curr = nums[i]
            temp_max_so_far = max(curr, max_so_far * curr, min_so_far * curr)
            min_so_far = min(curr, max_so_far * curr, min_so_far * curr)
            max_so_far = temp_max_so_far
            result = max(max_so_far, result)
        return result


def main() -> None:
    inputs = [[2, 3, -2, 4], [-2, 0, -1], [-2, 3, -4]]
    s = Solution()
    for nums in inputs:
        print(s.maxProduct(nums))


if __name__ == "__main__":
    main()
