from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, white, blue = 0, 0, len(nums) - 1
        while white <= blue:
            if nums[white] == 0:
                if nums[red] != 0:
                    nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                if nums[blue] != 2:
                    nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1


def main() -> None:
    inputs = [
        [2, 0, 2, 1, 1, 0],
        [2, 0, 1],
    ]

    s = Solution()
    for nums in inputs:
        s.sortColors(nums)
        print(nums)


if __name__ == "__main__":
    main()
