class Solution:
    def get_word_till_space(self, start, s):
        word = ""
        while start < len(s) and s[start] != " ":
            word += s[start]
            start += 1
        return word, start + 1

    def wordPattern(self, pattern: str, s: str) -> bool:
        d = {}
        start = 0
        idx = 0
        seen = set()
        while start < len(s) and idx < len(pattern):
            word, start = self.get_word_till_space(start, s)
            if pattern[idx] in d:
                if d[pattern[idx]] != word:
                    return False
            else:
                if word in seen:
                    return False
                seen.add(word)
                d[pattern[idx]] = word
            idx += 1
        return idx == len(pattern) and start >= len(s)


class Solution2:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        return [*map(pattern.index, pattern)] == [*map(s.index, s)]


if __name__ == "__main__":
    inputs = [
        ("abba", "dog cat cat dog"),
        ("abba", "dog cat cat fish"),
        ("aaaa", "dog cat cat dog"),
        ("abba", "sdsd sdsd sdsd sdsd"),
        ("aaaa", "aa aa aa aa"),
    ]
    s = Solution()
    for pattern, string in inputs:
        print(s.wordPattern(pattern, string))
