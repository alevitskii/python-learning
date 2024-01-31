class Solution:
    def reverseBits(self, n: int) -> int:
        return int(bin(n)[2:].zfill(32)[::-1], 2)


class Solution2:
    def reverseBits(self, n: int) -> int:
        return int(format(n, "b").zfill(32)[::-1], 2)


class Solution3:
    def reverseBits(self, n: int) -> int:
        new_n = 0
        for _ in range(32):
            new_n <<= 1
            if n & 1:
                new_n ^= 1
            n >>= 1
        return new_n


class Solution4:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31 - i))
        return res


if __name__ == "__main__":
    inputs = [
        43261596,
        4294967293,
    ]
    s = Solution4()
    for n in inputs:
        print(s.reverseBits(n))
