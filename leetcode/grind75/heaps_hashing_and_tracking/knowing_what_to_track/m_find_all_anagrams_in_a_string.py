from collections import defaultdict
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        p_counter = {}
        for c in p:
            if c not in p_counter:
                p_counter[c] = 0
            p_counter[c] += 1
        window_counter = {}
        for i in range(len(p)):
            if s[i] not in window_counter:
                window_counter[s[i]] = 0
            window_counter[s[i]] += 1
        result = []
        for i in range(len(p), len(s)):
            if window_counter == p_counter:
                result.append(i - len(p))
            window_counter[s[i - len(p)]] -= 1
            if window_counter[s[i - len(p)]] == 0:
                del window_counter[s[i - len(p)]]
            if s[i] not in window_counter:
                window_counter[s[i]] = 0
            window_counter[s[i]] += 1
        if window_counter == p_counter:
            result.append(i - len(p) + 1)
        return result


class Solution2:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        ans = []
        hash_s = defaultdict(int)
        hash_p = defaultdict(int)
        for c in p:
            hash_p[c] += 1
        for window_end in range(len(s)):
            hash_s[s[window_end]] += 1
            if window_end >= len(p):
                window_start = window_end - len(p)
                if hash_s[s[window_start]] == 1:
                    del hash_s[s[window_start]]
                else:
                    hash_s[s[window_start]] -= 1
            if hash_s == hash_p:
                start_index = window_end - len(p) + 1
                ans.append(start_index)
        return ans


def main() -> None:
    inputs = [
        ("cbaebabacd", "abc"),
        ("abab", "ab"),
    ]
    s = Solution2()
    for string, q in inputs:
        print(s.findAnagrams(string, q))


if __name__ == "__main__":
    main()
