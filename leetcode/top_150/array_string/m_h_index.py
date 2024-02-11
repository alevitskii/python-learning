from typing import List


class Solution0:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        h = 0
        for i in range(len(citations) - 1, -1, -1):
            h = max(h, min(citations[i], len(citations) - i))
        return h


class Solution01:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        h = 0
        for i in range(len(citations) - 1, -1, -1):
            cur_h = min(citations[i], len(citations) - i)
            if cur_h < h:
                return h
            h = cur_h
        return h


def main() -> None:
    inputs = [[3, 0, 6, 1, 5], [1, 3, 1], [5]]
    s = Solution01()
    for citations in inputs:
        print(s.hIndex(citations))


if __name__ == "__main__":
    main()
