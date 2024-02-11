from typing import List


# j = 0..len(nums)-1
# j = 0 -> 1 << j == 001
# j = 1 -> 1 << j == 010
# j = 2 -> 1 << j == 100
# 2**3 -> 000, 001, 010, 011, 100, 101, 110, 111
# 000 & 001 == 000, 000 & 010 == 000, 000 & 100 == 000 -> j = []
# 001 & 001 == 001, 001 & 010 == 000, 001 & 100 == 000 -> j = [0]
# 010 & 001 == 000, 010 & 010 == 010, 010 & 100 == 000 -> j = [1]
# 011 & 001 == 001, 011 & 010 == 010, 011 & 100 == 000 -> j = [0, 1]
# 100 & 001 == 000, 100 & 010 == 000, 100 & 100 == 100 -> j = [2]
# 101 & 001 == 001, 101 & 010 == 000, 101 & 100 == 100 -> j = [0, 2]
# 110 & 001 == 000, 110 & 010 == 010, 110 & 100 == 100 -> j = [0, 1]
# 111 & 001 == 001, 111 & 010 == 010, 111 & 100 == 100 -> j = [0, 1, 2]
class Solution:
    def get_bit(self, i, j):
        return (1 << j) & i != 0

    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        subsets_count = 2 ** len(nums)
        for i in range(subsets_count):
            subset = set()
            for j in range(len(nums)):
                if self.get_bit(i, j) and nums[j] not in subset:
                    subset.add(nums[j])
            subsets.append(list(subset))
        return subsets


class Solution2:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for num in nums:
            for i in range(len(subsets)):
                new_subset = subsets[i].copy()
                new_subset.append(num)
                subsets.append(new_subset)
        return subsets


def main() -> None:
    inputs = [
        [1, 2, 3],
        [0],
        [],
    ]
    s = Solution()
    for nums in inputs:
        print(s.subsets(nums))


if __name__ == "__main__":
    main()
