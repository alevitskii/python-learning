class Solution:
    def intToRoman(self, num: int) -> str:
        _map = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M",
        }
        lst = sorted(_map.keys())
        lst.reverse()
        res = ""
        while num:
            for number in lst:
                n = num // number
                if n >= 1:
                    res += n * _map[number]
                    num -= n * number
                    break
        return res


class Solution2:
    def intToRoman(self, num: int) -> str:
        num_map = {
            1: "I",
            5: "V",
            4: "IV",
            10: "X",
            9: "IX",
            50: "L",
            40: "XL",
            100: "C",
            90: "XC",
            500: "D",
            400: "CD",
            1000: "M",
            900: "CM",
        }
        r = ""
        for n in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
            while n <= num:
                r += num_map[n]
                num -= n
        return r


def main() -> None:
    inputs = [3, 58, 1994, 1, 1998, 2000, 3999]
    s = Solution()
    for num in inputs:
        print(s.intToRoman(num))


if __name__ == "__main__":
    main()
