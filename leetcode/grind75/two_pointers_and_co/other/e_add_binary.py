class Solution:
    def addBinary(self, a: str, b: str) -> str:
        q = False
        a = a[::-1]
        b = b[::-1]
        lst = max(len(a), len(b))
        s = ""
        for i in range(lst):
            if i > len(a) - 1:
                if q:
                    if b[i] == "1":
                        s += "0"
                    else:
                        s += "1"
                        q = False
                else:
                    s += b[i]
            elif i > len(b) - 1:
                if q:
                    if a[i] == "1":
                        s += "0"
                    else:
                        s += "1"
                        q = False
                else:
                    s += a[i]
            else:
                if {"0", "1"} == {a[i], b[i]}:
                    if q:
                        s += "0"
                        q = True
                    else:
                        s += "1"
                elif {"1", "1"} == {a[i], b[i]}:
                    if q:
                        s += "1"
                    else:
                        s += "0"
                    q = True
                elif {"0", "0"} == {a[i], b[i]}:
                    s += "1" if q else "0"
                    q = False

        return "1" + s[::-1] if q else s[::-1]


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


class Solution3:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0
        ptr1 = len(a) - 1
        ptr2 = len(b) - 1
        while ptr1 >= 0 or ptr2 >= 0:
            if ptr1 >= 0:
                digit1 = ord(a[ptr1]) - ord("0")
            else:
                digit1 = 0
            if ptr2 >= 0:
                digit2 = ord(b[ptr2]) - ord("0")
            else:
                digit2 = 0
            total_sum = digit1 + digit2 + carry
            current_digit = total_sum % 2
            carry = total_sum // 2
            result.append(current_digit)
            ptr1 -= 1
            ptr2 -= 1
        if carry:
            result.append(carry)
        reversed_result = result[::-1]
        binary_sum = "".join(str(digit) for digit in reversed_result)
        return binary_sum


if __name__ == "__main__":
    inputs = [
        ("11", "1"),
        ("1010", "1011"),
    ]

    s = Solution3()
    for a, b in inputs:
        print(s.addBinary(a, b))
