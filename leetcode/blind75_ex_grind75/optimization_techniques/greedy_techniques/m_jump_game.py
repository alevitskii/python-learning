class Solution:
    def canJump(self, nums: list[int]) -> bool:
        start, start_idx = nums[0], 0
        for i, n in enumerate(nums):
            rem_steps = start + start_idx - i
            if rem_steps < 0:
                return False
            if rem_steps < n:
                start, start_idx = n, i
        return True


class Solution2:
    def canJump(self, nums: list[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0


def main() -> None:
    inputs = [
        [2, 3, 1, 1, 4],
        [3, 2, 1, 0, 4],
        [1, 2, 3],
        [1, 0, 0],
        [5, 0, 0, 0, 0, 0, 0],
    ]

    s = Solution()
    for nums in inputs:
        print(s.canJump(nums))


if __name__ == "__main__":
    main()
