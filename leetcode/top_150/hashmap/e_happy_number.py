class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        calc = sum([int(i) ** 2 for i in list(str(n))])
        while calc not in seen:
            seen.add(calc)
            calc = sum([int(i) ** 2 for i in list(str(calc))])
        return calc == 1


class Solution2:
    def squares(self, n):
        return sum([int(i) ** 2 for i in list(str(n))])

    def isHappy(self, n: int) -> bool:
        slow = self.squares(n)
        fast = slow
        while True:
            slow = self.squares(slow)
            fast = self.squares(fast)
            if fast == 1:
                return True
            fast = self.squares(fast)
            if slow == fast:
                return False


if __name__ == "__main__":
    inputs = [
        19,
        2,
    ]
    s = Solution2()
    for n in inputs:
        print(s.isHappy(n))
