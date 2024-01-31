# "a)bc(d)" => "abc(d)"
# "(ab(c)a" => "ab(c)a" or "(abc)a"
# "))((" => ""
# "())()(((" => "()()"


# T: O(n), S: O(n)
def min_remove_to_make_valid(string):
    stack = []
    result = list(string)
    for i in range(len(result)):
        if result[i] == "(":
            stack.append(i)
        elif result[i] == ")" and len(stack):
            stack.pop()
        elif result[i] == ")":
            result[i] = ""
    while len(stack):
        result[stack.pop()] = ""
    return "".join(result)


if __name__ == "__main__":
    inputs = ["a)bc(d)", "(ab(c)a", "))((", "())()((("]
    for string in inputs:
        print(min_remove_to_make_valid(string))
