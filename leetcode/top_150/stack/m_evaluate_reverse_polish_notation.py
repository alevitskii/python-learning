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


class Solution2:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                match token:
                    case "+":
                        stack.append(num1 + num2)
                    case "-":
                        stack.append(num2 - num1)
                    case "*":
                        stack.append(num1 * num2)
                    case "/":
                        stack.append(int(num2 / num1))
        return stack[0]


def main() -> None:
    inputs = [
        ["2", "1", "+", "3", "*"],
        ["4", "13", "5", "/", "+"],
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"],
    ]
    s = Solution2()
    for tokens in inputs:
        print(s.evalRPN(tokens))


if __name__ == "__main__":
    main()
