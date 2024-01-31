import math


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return x
        sqrt = x / 2
        while True:
            prev = sqrt
            sqrt = (sqrt + x / sqrt) / 2
            if abs(prev - sqrt) < 1:
                break
        return math.floor(sqrt)


class Solution2:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            if square == x:
                return mid
            elif square < x:
                left = mid + 1
            else:
                right = mid - 1
        return right


if __name__ == "__main__":
    inputs = [4, 8, 1024, 8192]
    s = Solution()
    for n in inputs:
        print(s.mySqrt(n))
