# Brian Kernighan's Algorithm
class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n != 0:
            n &= n - 1
            cnt += 1
        return cnt


def main() -> None:
    inputs = [11, 128, 4294967293]
    s = Solution()
    for n in inputs:
        print(s.hammingWeight(n))


if __name__ == "__main__":
    main()
