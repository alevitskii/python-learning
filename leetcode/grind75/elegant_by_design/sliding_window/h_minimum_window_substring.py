from collections import defaultdict


class Solution:
    def valid(self, t_freq, window_freq):
        for c in t_freq:
            if c not in window_freq or t_freq[c] > window_freq[c]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        t_freq = defaultdict(int)
        for c in t:
            t_freq[c] += 1
        window_freq = defaultdict(int)
        left, right = 0, 0
        min_sub = ""
        while left < len(s):
            valid = self.valid(t_freq, window_freq)
            while right < len(s) and not valid:
                window_freq[s[right]] += 1
                right += 1
                valid = self.valid(t_freq, window_freq)
            if valid and (not min_sub or len(min_sub) > right - left):
                min_sub = s[left:right]
            window_freq[s[left]] -= 1
            left += 1
        return min_sub


class Solution2:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        req_count = {}
        window = {}
        for c in t:
            req_count[c] = 1 + req_count.get(c, 0)
        for c in t:
            window[c] = 0
        current, required = 0, len(req_count)
        res, res_len = [-1, -1], float("infinity")
        left = 0
        for right in range(len(s)):
            c = s[right]
            if c in t:
                window[c] = 1 + window.get(c, 0)
            if c in req_count and window[c] == req_count[c]:
                current += 1
            while current == required:
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1
                if s[left] in t:
                    window[s[left]] -= 1
                if s[left] in req_count and window[s[left]] < req_count[s[left]]:
                    current -= 1
                left += 1
        left, right = res
        return s[left : right + 1] if res_len != float("infinity") else ""


if __name__ == "__main__":
    inputs = [
        ("ADOBECODEBANC", "ABC"),
        ("a", "a"),
        ("a", "aa"),
    ]
    s = Solution2()
    for string, t in inputs:
        print(s.minWindow(string, t))
