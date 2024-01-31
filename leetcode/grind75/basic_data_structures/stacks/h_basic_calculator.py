class Solution:
    def calculate(self, s: str) -> int:
        number = 0
        sign_value = 1
        result = 0
        operations_stack = []
        for c in s:
            if c.isdigit():
                number = number * 10 + int(c)
            if c in "+-":
                result += number * sign_value
                sign_value = -1 if c == "-" else 1
                number = 0
            elif c == "(":
                operations_stack.append(result)
                operations_stack.append(sign_value)
                result = 0
                sign_value = 1
            elif c == ")":
                result += sign_value * number
                pop_sign_value = operations_stack.pop()
                result *= pop_sign_value
                second_value = operations_stack.pop()
                result += second_value
                number = 0
        return result + number * sign_value


if __name__ == "__main__":
    inputs = [
        "1 + 1",
        " 2-1 + 2 ",
        "(1+(4+5+2)-3)+(6+8)",
    ]
    s = Solution()
    for string in inputs:
        print(s.calculate(string))
