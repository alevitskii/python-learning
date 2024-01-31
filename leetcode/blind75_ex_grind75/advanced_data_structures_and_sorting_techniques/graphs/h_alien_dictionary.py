from collections import Counter, defaultdict, deque
from typing import List


class Solution:
    def alienDict(self, words: List[str]) -> str:
        adj_list = defaultdict(set)
        counts = Counter({c: 0 for word in words for c in word})
        outer = 0
        for word1, word2 in zip(words, words[1:]):
            outer += 1
            inner = 0
            for c, d in zip(word1, word2):
                inner += 1
                if c != d:
                    if d not in adj_list[c]:
                        adj_list[c].add(d)
                        counts[d] += 1
                    break
            else:
                if len(word2) < len(word1):
                    return ""
        result = []
        sources_queue = deque([c for c in counts if counts[c] == 0])
        while sources_queue:
            c = sources_queue.popleft()
            result.append(c)
            for d in adj_list[c]:
                counts[d] -= 1
                if counts[d] == 0:
                    sources_queue.append(d)
        if len(result) < len(counts):
            return ""
        return "".join(result)


if __name__ == "__main__":
    inputs = [
        ["xro", "xma", "per", "prt", "oxh", "olv"],
        ["mdx", "mars", "avgd", "dkae"],
    ]
    s = Solution()
    for words in inputs:
        print(s.alienDict(words))
