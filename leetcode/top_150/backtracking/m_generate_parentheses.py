from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def recursion(current, openning, closing):
            if not openning and not closing:
                result.append(current)
                return
            if not openning:
                recursion(current + ")" * closing, openning, 0)
            elif openning == closing:
                recursion(current + "(", openning - 1, closing)
            else:
                recursion(current + "(", openning - 1, closing)
                recursion(current + ")", openning, closing - 1)

        result = []
        recursion("", n, n)
        return result


class Solution2:
    def generateParenthesis(self, n: int) -> List[str]:
        def recursion(current, openning, closing):
            if len(current) == 2 * n:
                result.append(current)
                return
            if openning < n:
                recursion(current + "(", openning + 1, closing)
            if openning < closing:
                recursion(current + ")", openning, closing + 1)

        result = []
        recursion("", 0, 0)
        return result


if __name__ == "__main__":
    inputs = [
        3,
        # 1,
    ]
    s = Solution()
    for n in inputs:
        print(s.generateParenthesis(n))
