class Solution:
    def romanToInt(self, s: str) -> int:
        roman2int = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }
        idx = 0
        number = 0
        while idx < len(s):
            if s[idx : idx + 2] in roman2int:
                number += roman2int[s[idx : idx + 2]]
                idx += 2
            else:
                curr_char = s[idx]
                while idx < len(s) and curr_char == s[idx]:
                    number += roman2int[curr_char]
                    idx += 1
        return number


class Solution2:
    def romanToInt(self, s: str) -> int:
        m = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        ans = 0
        for i in range(len(s)):
            if i < len(s) - 1 and m[s[i]] < m[s[i + 1]]:
                ans -= m[s[i]]
            else:
                ans += m[s[i]]
        return ans


def main() -> None:
    inputs = ["III", "LVIII", "MCMXCIV"]
    s = Solution()
    for string in inputs:
        print(s.romanToInt(string))


if __name__ == "__main__":
    main()
