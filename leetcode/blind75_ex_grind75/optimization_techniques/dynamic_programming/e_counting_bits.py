from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        curr_pow2, next_pow2 = 0, 1
        ans = [0]
        for i in range(1, n + 1):
            if i == next_pow2:
                curr_pow2, next_pow2 = next_pow2, next_pow2 * 2
                ans.append(1)
            else:
                ans.append(ans[curr_pow2] + ans[i - curr_pow2])
        return ans


class Solution2:
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n + 1)
        if n == 0:
            return result
        result[0:2] = (0, 1)
        for x in range(2, n + 1):
            # a * 2 == a << 1
            if x % 2 == 0:
                result[x] = result[x // 2]
            else:
                result[x] = result[x // 2] + 1
        return result


if __name__ == "__main__":
    inputs = [0, 1, 2, 5, 10]
    s = Solution2()
    for n in inputs:
        print(s.countBits(n))
