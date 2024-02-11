import string
from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        myset = set(wordList)
        if endWord not in myset:
            return 0
        q = deque()
        q.append(beginWord)
        length = 0
        while q:
            length += 1
            size = len(q)
            for _ in range(size):
                curr = q.popleft()
                for i in range(len(curr)):
                    for c in string.ascii_lowercase:
                        temp = list(curr)
                        temp[i] = c
                        temp = "".join(temp)
                        if temp == endWord:
                            return length + 1
                        if temp in myset:
                            q.append(temp)
                            myset.remove(temp)
        return 0


def main() -> None:
    inputs = [
        ("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]),
        ("hit", "cog", ["hot", "dot", "dog", "lot", "log"]),
    ]
    s = Solution()
    for beginWord, endWord, wordList in inputs:
        print(s.ladderLength(beginWord, endWord, wordList))


if __name__ == "__main__":
    main()
