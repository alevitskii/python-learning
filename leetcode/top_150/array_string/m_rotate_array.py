from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        if k == 0:
            return
        for i in range(0, len(nums), k):
            slice_range = min(i + k, len(nums) - k)
            nums[i:slice_range], nums[len(nums) - k :] = nums[len(nums) - k :], nums[i:slice_range]
            if len(nums) - k < i + k:
                break


class Solution2:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]


class Solution3:
    def rotate(self, nums: List[int], k: int) -> None:
        L = len(nums)
        if L == k:
            return

        k %= L
        nums.reverse()

        for i in range(k // 2):
            nums[i], nums[k - 1 - i] = nums[k - 1 - i], nums[i]

        for i in range(k, (L + k) // 2):
            nums[i], nums[L - 1 - i + k] = nums[L - 1 - i + k], nums[i]

        # for i in range((L - k) // 2):
        #     nums[i + k], nums[L - 1 - i] = nums[L - 1 - i], nums[i + k]


# [1, 2, 3, 4, 5, 6, 7]
# [7, 6, 5, 4, 3, 2, 1]
# [5, 6, 7, 1, 2, 3, 4]


def main() -> None:
    inputs = [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 4),
        ([-1, -100, 3, 99], 2),
        ([1, 2, 3, 4, 5, 6, 7], 3),  # [5, 6, 7, 1, 2, 3, 4]
        ([-1, -100], 1),
        ([-1], 1),
        ([-1], 0),
    ]
    s = Solution3()
    for nums, k in inputs:
        print(s.rotate(nums, k))
        print(nums)


if __name__ == "__main__":
    main()
