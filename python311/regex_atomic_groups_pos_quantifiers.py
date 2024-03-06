import re


def main() -> None:
    # atomic groups
    reg = re.compile(r"a(?>bc|b)c")
    print(reg.match("abcc"))
    # it'll match 'a', then it'll find the first match from atomic group 'bc'
    # and close the group, then it'll try to find 'c' and it won't
    # so it disables backtracking
    print(reg.match("abc"))

    # possesive quantifiers: .++, .*+, .?+, .{2}+ etc
    # also disables backtracking
    reg = re.compile(r'".++"')
    reg2 = re.compile(r'"[^"]++"')
    print(reg.match('"foo"'))
    print(reg2.match('"foo"'))


if __name__ == "__main__":
    main()
