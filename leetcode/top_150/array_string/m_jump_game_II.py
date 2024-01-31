from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        goal = len(nums) - 1
        jumps = 0
        while True:
            for i in range(goal):
                if i + nums[i] >= goal:
                    goal = i
                    jumps += 1
                    break
            if goal == 0:
                return jumps


class Solution2:
    def jump(self, nums: List[int]) -> int:
        jumps, segment_end = 0, 0
        next_farthest = 0
        for i in range(len(nums) - 1):
            next_farthest = max(next_farthest, i + nums[i])
            if next_farthest >= len(nums) - 1:
                return jumps + 1
            if i == segment_end:
                segment_end = next_farthest
                jumps += 1
        return jumps


if __name__ == "__main__":
    inputs = [
        [2, 3, 1, 1, 4],
        [2, 3, 0, 1, 4],
        [2, 1, 1],
    ]
    s = Solution()
    for nums in inputs:
        print(s.jump(nums))
