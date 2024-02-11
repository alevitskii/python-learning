class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        original, reverted = x, 0
        while original != 0:
            reverted = reverted * 10 + original % 10
            original //= 10
        return reverted == x


def main() -> None:
    inputs = [121, -121, 10]
    s = Solution()
    for n in inputs:
        print(s.isPalindrome(n))


if __name__ == "__main__":
    main()
