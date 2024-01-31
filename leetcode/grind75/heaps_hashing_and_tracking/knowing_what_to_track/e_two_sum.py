class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen_numbers = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in seen_numbers:
                return [seen_numbers[diff], i]
            seen_numbers[n] = i
        return


if __name__ == "__main__":
    inputs = [
        ([2, 7, 11, 15], 9),
        ([3, 2, 4], 6),
        ([3, 3], 6),
    ]
    s = Solution()
    for nums, target in inputs:
        print(s.twoSum(nums, target))
