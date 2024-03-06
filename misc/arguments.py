"""
        Left side                  Divider            Right side
Positional-only arguments             /       Positional or keyword arguments
Positional or keyword arguments	      *       Keyword-only arguments
"""


# takes positional only
def positional(x, y, /):
    print(f"{x=}, {y=}")


# can take 3 positional or 2 pos and 1 kw
def only_2_positional(x, y, /, z):
    print(f"{x=}, {y=}")


def two_pos_one_kw(x, y, /, *, kw):
    print(f"{x=}, {y=}, {kw=}")


# takes only keywords
def kwonly(*, kw):
    print(f"{kw=}")


def combination(a, /, b, c=2, *d, e=2, **kwargs):
    print(f"{a=}, {b=}, {c=}, {d=}, {e=} {kwargs=}")


def main() -> None:
    positional("123", 2)
    only_2_positional("123", 2, 3)
    kwonly(kw="123")
    two_pos_one_kw(1, 2, kw="123")
    combination(1, 2, 3, 5, 6, 7, e=8, h=1, i=10)


if __name__ == "__main__":
    main()
    import sys

    print("123", file=sys.stderr)
