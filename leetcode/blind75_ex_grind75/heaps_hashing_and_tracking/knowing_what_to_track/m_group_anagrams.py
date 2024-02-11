from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        idxs = defaultdict(list)
        for i, s in enumerate(strs):
            idxs[tuple(sorted(s))].append(i)
        return [[strs[i] for i in aidx] for aidx in idxs.values()]


class Solution2:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        idxs = defaultdict(list)
        for s in strs:
            f = [0] * 26
            for c in s:
                f[ord(c) - ord("a")] += 1
            idxs[tuple(f)].append(s)
        return list(idxs.values())


def main() -> None:
    inputs = [["eat", "tea", "tan", "ate", "nat", "bat"], [""], ["a"]]
    s = Solution2()
    for strs in inputs:
        print(s.groupAnagrams(strs))


if __name__ == "__main__":
    main()
