class Solution:
    def myAtoi(self, s: str) -> int:
        result = 0
        sign = 1
        i = 0
        while i < len(s) and s[i] == " ":
            i += 1
        if i < len(s) and (s[i] == "-" or s[i] == "+"):
            if s[i] == "-":
                sign = -1
            i += 1
        while i < len(s) and "0" <= s[i] <= "9":
            digit = ord(s[i]) - ord("0")
            if result > (2**31 - 1 - digit) // 10:
                return sign * (2**31 - 1) if sign == 1 else sign * (2**31)
            result = result * 10 + digit
            i += 1
        return sign * result


if __name__ == "__main__":
    inputs = [
        "42",
        "   -42",
        "4193 with words",
    ]

    s = Solution()
    for string in inputs:
        print(s.myAtoi(string))
