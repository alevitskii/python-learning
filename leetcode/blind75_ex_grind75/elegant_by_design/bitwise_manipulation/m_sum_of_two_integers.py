class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        while b != 0:
            result = (a ^ b) & mask
            carry = ((a & b) << 1) & mask
            a = result
            b = carry
        max_int = 0x7FFFFFFF
        if a < max_int:
            return a
        else:
            return ~(a ^ mask)


if __name__ == "__main__":
    inputs = [
        (1, 2),
        (2, 3),
    ]
    s = Solution()
    for a, b in inputs:
        print(s.getSum(a, b))
