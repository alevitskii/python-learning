from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def recursive(src, perm):
            if len(src) == 0:
                result.append(perm.copy())
                return
            for i in range(len(src)):
                perm.append(src[i])
                recursive(src[:i] + src[i + 1 :], perm)
                perm.pop()

        result = []
        recursive(nums, [])
        return result


class Solution2:
    def swap_char(self, nums, i, j):
        swap_index = nums.copy()
        swap_index[i], swap_index[j] = swap_index[j], swap_index[i]
        return swap_index

    def permute_rec(self, nums, current_index, result):
        if current_index == len(nums) - 1:
            result.append(nums)
            return
        for i in range(current_index, len(nums)):
            swapped_str = self.swap_char(nums, current_index, i)
            self.permute_rec(swapped_str, current_index + 1, result)

    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.permute_rec(nums, 0, result)
        return result


# [1, 2, 3]
# 1. Fix 1, work with [2, 3]
# 1.1. Fix 2, work with 3           -> [1, 2, 3]
# 1.2. Swap 2 and 3, work with 2    -> [1, 3, 2]
# 2. Swap 1 and 2, work with [1, 3]
# 2.1. Fix 1, work with 3           -> [2, 1, 3]
# 2.2. Swap 1 and 3, work with 1    -> [2, 3, 1]
# 3. Swap 1 and 3, work with [2, 1]
# 3.1. Fix 2, work with 1           -> [3, 2, 1]
# 3.2. Swap 2 and 1, work with 2    -> [3, 1, 2]


if __name__ == "__main__":
    inputs = [[1, 2, 3], [0, 1], [1]]
    s = Solution2()
    for nums in inputs:
        print(s.permute(nums))
