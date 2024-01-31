# S: "ab#z", T: "az#z", answer = True
# S: "abc#d", T: "acc#c", answer = False
# S: "x#y#z#", T: "a#", answer = True
# S: "x###b", T: "b", answer = True
# S: "Ab#z", T: "ab#z", answer = False


def build_string(string):
    built_array = []
    for i in string:
        if i == "#" and len(built_array) > 0:
            built_array.pop()
        elif i != "#":
            built_array.append(i)
    return built_array


# T: O(2m+k) or O(m+2k) ~ O(m+k), S: O(m+k)
def backspace_compare(s, t):
    final_s = build_string(s)
    final_t = build_string(t)

    if len(final_s) != len(final_t):
        return False

    for i in range(len(final_s)):
        if final_s[i] != final_t[i]:
            return False

    return True


# T: O(m+k), S: O(1)
def backspace_compare_p(s, t):
    s_index, t_index = len(s) - 1, len(t) - 1
    while s_index >= 0 or t_index >= 0:
        if s[s_index] == "#" or t[t_index] == "#":
            if s[s_index] == "#":
                backcount = 2
                while backcount > 0:
                    s_index -= 1
                    backcount -= 1
                    if s_index >= 0 and s[s_index] == "#":
                        backcount += 2
            if t[t_index] == "#":
                backcount = 2
                while backcount > 0:
                    t_index -= 1
                    backcount -= 1
                    if t_index >= 0 and t[t_index] == "#":
                        backcount += 2
        else:
            if s[s_index] != t[t_index]:
                return False
            s_index -= 1
            t_index -= 1
    return True


if __name__ == "__main__":
    inputs = [
        ("ab#z", "az#z"),
        ("abc#d", "acc#c"),
        ("x#y#z#", "a#"),
        ("x###b", "b"),
        ("Ab#z", "ab#z"),
    ]
    for s, t in inputs:
        print(backspace_compare(s, t))
        print(backspace_compare_p(s, t))
