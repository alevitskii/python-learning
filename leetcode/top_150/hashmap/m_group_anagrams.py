from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        idxs = defaultdict(list)
        for i, s in enumerate(strs):
            idxs[tuple(sorted(s))].append(i)
        return [[strs[i] for i in aidx] for aidx in idxs.values()]


def main() -> None:
    inputs = [["eat", "tea", "tan", "ate", "nat", "bat"], [""], ["a"]]
    s = Solution()
    for strs in inputs:
        print(s.groupAnagrams(strs))


if __name__ == "__main__":
    main()
