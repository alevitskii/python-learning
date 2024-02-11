from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)


class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        records = {}
        for i in nums:
            if i in records:
                return True
            records[i] = i
        return False


def main() -> None:
    inputs = [
        [1, 2, 3, 1],
        [1, 2, 3, 4],
        [1, 1, 1, 3, 3, 4, 3, 2, 4, 2],
    ]
    s = Solution2()
    for nums in inputs:
        print(s.containsDuplicate(nums))


if __name__ == "__main__":
    main()
