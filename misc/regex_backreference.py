import re


def main() -> None:
    pat_wrong = re.compile(r'[\'"].*[\'"]')
    print(pat_wrong.match("'foo\""))

    pat = re.compile(r'([\'"]).*\1')  # \0 matches the whole string
    print(pat.match("'foo\""))
    print(pat.match("'foo'"))
    print(pat.match('"foo"'))

    pat = re.compile(r'(?P<quote>[\'"]).*(?P=quote)')  # named group
    match = pat.match('"foo"')
    print(match[1], match["quote"], match.group(1), match.group("quote"))

    pat = re.compile(r'(?P<quote>[\'"])(?P<meat>.*)(?P=quote)')
    pat.match('"foo"')
    match = pat.match('"foo"')
    print(match["meat"])
    print(match["quote"])

    print(pat.sub(r"\1hello \2\1", '"foo"'))
    print(pat.sub(r"\g<quote>hello \g<meat>\g<quote>", '"foo"'))
    print(pat.sub(r"\g<1>hello \g<2>\g<1>", '"foo"'))

    print(pat.sub(r"\1123deadbeaf \2\1", '"foo"'))
    print(pat.sub(r"\g<1>123deadbeaf \2\1", '"foo"'))


if __name__ == "__main__":
    main()
