from collections import defaultdict
from typing import List


# Boyer-Moore’s voting algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        for n in nums:
            if count == 0:
                candidate = n
            count += 1 if n == candidate else -1
        return candidate


class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        records = defaultdict(int)
        for item in nums:
            records[item] += 1
        return max(records.keys(), key=records.get)


if __name__ == "__main__":
    inputs = [
        [3, 2, 3],
        [2, 2, 1, 1, 1, 2, 2],
    ]
    s = Solution()
    for nums in inputs:
        print(s.majorityElement(nums))
