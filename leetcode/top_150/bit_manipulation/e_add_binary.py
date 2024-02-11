class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carrier = 0
        aidx, bidx = len(a) - 1, len(b) - 1
        res = ""
        while aidx >= 0 and bidx >= 0:
            bita, bitb = int(a[aidx]), int(b[bidx])
            n = bita + bitb + carrier
            if n == 3:
                res += "1"
                carrier = 1
            elif n == 2:
                if carrier == 0:
                    carrier = 1
                res += "0"
            elif n == 1:
                if carrier == 1:
                    carrier = 0
                res += "1"
            else:
                res += "0"
            aidx -= 1
            bidx -= 1
        while aidx >= 0:
            if a[aidx] == "1":
                res += "0" if carrier else "1"
            else:
                if carrier:
                    res += "1"
                    carrier = 0
                else:
                    res += "0"
            aidx -= 1
        while bidx >= 0:
            if b[bidx] == "1":
                res += "0" if carrier else "1"
            else:
                if carrier:
                    res += "1"
                    carrier = 0
                else:
                    res += "0"
            bidx -= 1

        res += "1" if carrier else ""
        return res[::-1]


class Solution2:
    def addBinary(self, a: str, b: str) -> str:
        s = []
        carry = 0
        i = len(a) - 1
        j = len(b) - 1
        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1
            s.append(str(carry % 2))
            carry //= 2
        return "".join(reversed(s))


def main() -> None:
    inputs = [
        ("11", "1"),
        ("1010", "1011"),
        ("1", "1"),
        ("1", "0"),
        ("100", "110010"),
    ]
    s = Solution2()
    for a, b in inputs:
        print(s.addBinary(a, b))


if __name__ == "__main__":
    main()
