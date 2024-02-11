from typing import List


# [2, 2, 2, 3]
# 0: seen_once = 00, seen_twice = 00
# 1 (2): seen_once = 10, seen_twice = 00
# 2 (2): seen_once = 00: seen_twice == 10
# 3 (2): seen_once = 00, seen_twice = 00
# 4 (3): seen_once = 11, seen_twice = 00
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen_once = seen_twice = 0
        for num in nums:
            seen_once = ~seen_twice & (seen_once ^ num)
            seen_twice = ~seen_once & (seen_twice ^ num)
        return seen_once


def main() -> None:
    inputs = [
        [2, 2, 3, 2],
        [0, 1, 0, 1, 0, 1, 99],
    ]
    s = Solution()
    for n in inputs:
        print(s.singleNumber(n))


if __name__ == "__main__":
    main()
