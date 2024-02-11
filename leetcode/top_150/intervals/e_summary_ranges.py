from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        def construct_range(left, right):
            return f"{left}->{right}" if left < right else str(left)

        if not nums:
            return nums

        left, right = nums[0], nums[0]
        result = []
        for i in range(1, len(nums)):
            if nums[i] - right > 1:
                result.append(construct_range(left, right))
                left = nums[i]
            right = nums[i]
        return result + [construct_range(left, right)]


class Solution2:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        def construct_range(left, right):
            return f"{left}->{right}" if left < right else str(left)

        if not nums:
            return nums

        left, right = nums[0], nums[0]
        result = []
        for i in range(len(nums) - 1):
            if right + 1 < nums[i + 1]:
                result.append(construct_range(left, right))
                left = right = nums[i + 1]
            right = nums[i + 1]
        return result + [construct_range(left, right)]


def main() -> None:
    inputs = [
        [0, 1, 2, 4, 5, 7],
        [0, 2, 3, 4, 6, 8, 9, 10],
        [0, 1],
        [],
    ]
    s = Solution2()
    for nums in inputs:
        print(s.summaryRanges(nums))


if __name__ == "__main__":
    main()
