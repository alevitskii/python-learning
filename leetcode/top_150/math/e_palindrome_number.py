class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        temp = x
        rev = 0
        while temp != 0:
            rem = temp % 10
            rev = rev * 10 + rem
            temp //= 10
        return rev == x


if __name__ == "__main__":
    inputs = [121, -121, 10]
    s = Solution()
    for n in inputs:
        print(s.isPalindrome(n))
