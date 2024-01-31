class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = [[set() for i in range(len(s))] for j in range(len(s))]
        res = 0
        for i in range(len(s)):
            m[i][i] = {s[i]}
            for j in range(i + 1, len(s)):
                if s[j] not in m[i][j - 1]:
                    m[i][j] = m[i][j - 1] | {s[j]}
                    res = max(j - i, res)
                else:
                    break
        return res + 1 if s else 0


class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        left, right = 0, 0
        while right < len(s):
            if s[right] not in s[left:right]:
                right += 1
                res = max(res, right - left)
            else:
                while s[right] in s[left:right]:
                    left += 1
        return res


class Solution3:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res, left = 0, 0
        char_set = set()
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            res = max(res, right - left + 1)
        return res


class Solution4:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        max_length = 0
        start, idx = 0, 0
        while idx < len(s):
            c = s[idx]
            max_length = max(idx - start, max_length)
            if c in seen and seen[c] >= start:
                start = seen[c] + 1
            seen[c] = idx
            idx += 1
        return max(idx - start, max_length)


class Solution5:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        longest = 0
        left, right = 0, 0
        seen_chars = {}
        for right in range(len(s)):
            current_char = s[right]
            prev_seen_char = seen_chars.get(current_char, -1)
            if prev_seen_char >= left:
                left = prev_seen_char + 1
            seen_chars[current_char] = right
            longest = max(longest, right - left + 1)
        return longest


class Solution6:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        window_start, longest, window_length = 0, 0, 0
        last_seen_at = {}
        idx = 0
        for idx, val in enumerate(s):
            if val not in last_seen_at:
                last_seen_at[val] = idx
            else:
                if last_seen_at[val] >= window_start:
                    window_length = idx - window_start
                    if longest < window_length:
                        longest = window_length
                    window_start = last_seen_at[val] + 1
                last_seen_at[val] = idx
        idx += 1
        if longest < idx - window_start:
            longest = idx - window_start
        return longest


if __name__ == "__main__":
    inputs = ["abcabcbb", "bbbbb", "pwwkew", "a", "abc", "cabb", ""]
    s = Solution2()
    for string in inputs:
        print(s.lengthOfLongestSubstring(string))
