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
                    alpha = "abcdefghijklmnopqrstuvwxyz"
                    for c in alpha:
                        temp = list(curr)
                        temp[i] = c
                        temp = "".join(temp)
                        if temp == endWord:
                            return length + 1
                        if temp in myset:
                            q.append(temp)
                            myset.remove(temp)
        return 0


if __name__ == "__main__":
    inputs = [
        ("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]),
        ("hit", "cog", ["hot", "dot", "dog", "lot", "log"]),
    ]
    s = Solution()
    for beginWord, endWord, wordList in inputs:
        print(s.ladderLength(beginWord, endWord, wordList))
