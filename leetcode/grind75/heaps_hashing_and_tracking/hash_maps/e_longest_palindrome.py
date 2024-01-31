from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        for k in s:
            if k not in d:
                d[k] = 0
            d[k] += 1
        evens = 0
        odd = 0
        for k in d:
            if d[k] % 2 == 0:
                evens += d[k]
            else:
                if d[k] > odd:
                    evens += odd - 1 if odd != 0 else odd
                    odd = d[k]
                else:
                    evens += d[k] - 1
        return evens + odd


class Solution2:
    def longestPalindrome(self, s: str) -> int:
        odd_count = 0
        d = {}
        for ch in s:
            if ch in d:
                d[ch] += 1
            else:
                d[ch] = 1
            if d[ch] % 2 == 1:
                odd_count += 1
            else:
                odd_count -= 1
        if odd_count > 1:
            return len(s) - odd_count + 1
        return len(s)


class Solution3:
    def longestPalindrome(self, s: str) -> int:
        char_count = Counter(s)
        length = 0

        for count in char_count.values():
            length += count // 2 * 2

        if length < len(s):
            length += 1

        return length


if __name__ == "__main__":
    inputs = [
        "abccccdd",
        "a",
        "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqm"
        "etonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingpla"
        "ceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatwesho"
        "ulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebra"
        "velmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgh"
        "eworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereIti"
        "sforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfa"
        "rsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromt"
        "hesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevo"
        "tionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshall"
        "haveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfro"
        "mtheearth",
    ]
    s = Solution3()
    for string in inputs:
        print(s.longestPalindrome(string))
