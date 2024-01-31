class Solution:
    # The isBadVersion API is already defined for you.
    def isBadVersion(self, version: int) -> bool:
        return version >= self.bad

    def firstBadVersion(self, n: int, bad: int) -> int:
        self.bad = bad
        left, right = 1, n

        while left < right:
            center = (left + left) >> 1
            if self.isBadVersion(center):
                right = center
            else:
                left = center + 1
        return left


if __name__ == "__main__":
    inputs = [
        (5, 4),
        (1, 1),
    ]

    s = Solution()
    for n, bad in inputs:
        print(s.firstBadVersion(n, bad))
