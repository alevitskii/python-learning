from collections import deque
from typing import List


# Timeout
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def jump(nums, pos, dp):
            if pos == len(nums) - 1:
                return True
            if pos >= len(nums):
                return False
            if pos not in dp:
                dp[pos] = set()
            for i in range(1, nums[pos] + 1):
                if i not in dp[pos]:
                    dp[pos].add(i)
                    reached = jump(nums, pos + i, dp)
                    if reached:
                        return True
            return False

        return jump(nums, 0, {})


# Timeout
class Solution2:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True
        queue = deque()
        queue.append(len(nums) - 1)
        while queue:
            idx = queue.popleft()
            for j in range(0, idx):
                if j + nums[j] >= idx:
                    if j == 0:
                        return True
                    queue.append(j)
        return False


class Solution3:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0


class Solution4:
    def canJump(self, nums):
        curr = nums[0]
        for i in range(1, len(nums)):
            if curr == 0:
                return False
            curr -= 1
            curr = max(curr, nums[i])
        return True


if __name__ == "__main__":
    inputs = [[2, 3, 1, 1, 4], [3, 2, 1, 0, 4], [3, 0, 0, 0, 1], [0], [9997] + list(range(9997, -1, -1)) + [0]]
    s = Solution3()
    for nums in inputs:
        print(s.canJump(nums))
