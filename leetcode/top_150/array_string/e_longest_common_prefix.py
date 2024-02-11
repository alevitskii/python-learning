from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for idx in range(1, len(strs)):
            string = strs[idx]
            min_length = min(len(string), len(prefix))
            new_prefix = ""
            for i in range(min_length):
                if string[i] != prefix[i]:
                    break
                new_prefix += prefix[i]
            prefix = new_prefix if len(new_prefix) < len(prefix) else prefix
        return prefix


class Solution2:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first, last = strs[0], strs[-1]
        idx, prefix = 0, ""
        min_length = min(len(first), len(last))
        while idx < min_length and first[idx] == last[idx]:
            prefix += first[idx]
            idx += 1
        return prefix


def main() -> None:
    inputs = [
        ["flower", "flow", "flight"],
        ["dog", "racecar", "car"],
        ["a"],
    ]
    s = Solution2()
    for strings in inputs:
        print(s.longestCommonPrefix(strings))


if __name__ == "__main__":
    main()
