from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2
        s = {0}
        for i in range(len(nums) - 1, -1, -1):
            nexts = set()
            for n in s:
                if n + nums[i] == target:
                    return True
                nexts.add(nums[i] + n)
                nexts.add(n)
            s = nexts
        return False


if __name__ == "__main__":
    inputs = [
        [1, 5, 11, 5],
        [1, 2, 3, 5],
        [1, 3, 7, 3],
    ]
    s = Solution()
    for string in inputs:
        print(s.canPartition(string))
