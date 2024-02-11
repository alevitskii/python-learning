class Solution:
    def climbStairs(self, n: int) -> int:
        prev, last = 1, 1
        cnt = 2
        while cnt < n + 1:
            prev, last = last, prev + last
            cnt += 1

        return last


class Solution2:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        lookup_table = [0 for x in range(n + 1)]
        lookup_table[1] = 1
        lookup_table[2] = 2
        for i in range(3, n + 1):
            lookup_table[i] = lookup_table[i - 1] + lookup_table[i - 2]
        return lookup_table[n]


def main() -> None:
    inputs = [
        2,
        3,
    ]
    s = Solution2()
    for n in inputs:
        print(s.climbStairs(n))


if __name__ == "__main__":
    main()
