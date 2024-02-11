from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def recursion(current, start, n, k):
            if len(current) == k:
                result.append(current)
                return
            for i in range(start, n):
                recursion(current + [i], i + 1, n, k)

        result = []
        recursion([], 1, n + 1, k)
        return result


def main() -> None:
    inputs = [
        (4, 2),
        (1, 1),
        (3, 3),
    ]
    s = Solution()
    for n, k in inputs:
        print(s.combine(n, k))


if __name__ == "__main__":
    main()
