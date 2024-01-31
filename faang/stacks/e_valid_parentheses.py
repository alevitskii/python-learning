# "" => True
# "{([])}" => True
# "{([]" => False
# "{[[])}" => False


# T: O(n), S: O(n)
def is_valid_parentheses(string):
    stack = []
    opposites = {"(": ")", "{": "}", "[": "]"}
    for i in string:
        if i in opposites:
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            left_bracket = stack.pop()
            if opposites[left_bracket] != i:
                return False
    return len(stack) == 0


if __name__ == "__main__":
    inputs = ["", "{([])}", "{([]", "{[[])}"]
    for string in inputs:
        print(string, is_valid_parentheses(string))
