from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        k = 0
        while idx < len(nums):
            if nums[idx] == val:
                p = idx + 1
                while p < len(nums):
                    if nums[p] != val:
                        nums[idx], nums[p] = nums[p], nums[idx]
                        break
                    p += 1
                else:
                    return k
            idx += 1
            k += 1
        return k


class Solution2:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        for i in nums:
            if i != val:
                nums[idx] = i
                idx += 1
        return idx


def main() -> None:
    inputs = [([0, 1, 2, 2, 3, 0, 4, 2], 2)]  # [0, 1, 4, 0, 3, _, _, _], 5
    s = Solution()
    s2 = Solution2()
    for nums, val in inputs:
        print(s2.removeElement(nums, val))
        print(nums)


if __name__ == "__main__":
    main()
