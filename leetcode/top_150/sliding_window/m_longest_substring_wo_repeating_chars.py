class Solution:
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


class Solution2:
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


if __name__ == "__main__":
    inputs = ["abcabcbb", "bbbbb", "pwwkew", "a", "abc", "cabb", ""]
    s = Solution()
    for string in inputs:
        print(s.lengthOfLongestSubstring(string))
