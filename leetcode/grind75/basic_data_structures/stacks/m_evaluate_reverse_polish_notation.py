from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                if token == "+":
                    stack.append(num1 + num2)
                if token == "-":
                    stack.append(num2 - num1)
                if token == "*":
                    stack.append(num1 * num2)
                if token == "/":
                    stack.append(int(num2 / num1))
        return stack[0]


if __name__ == "__main__":
    inputs = [
        ["2", "1", "+", "3", "*"],
        ["4", "13", "5", "/", "+"],
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"],
    ]
    s = Solution()
    for tokens in inputs:
        print(s.evalRPN(tokens))
