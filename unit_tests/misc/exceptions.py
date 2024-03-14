import pytest


class VersionError(ValueError):
    pass


def parse_version(s: str) -> tuple[int, int]:
    ret = tuple(int(part) for part in s.split("."))
    if len(ret) != 2:
        raise VersionError(f"Expected #.# but got {s!r}")
    return ret


@pytest.mark.parametrize(
    ("input_s", "expected"),
    (("2.7", (2, 7)), ("3.6", (3, 6)), ("3.10", (3, 10))),
)
def test_parse_version(input_s, expected):
    assert parse_version(input_s) == expected


def test_parse_version_not_a_number():
    with pytest.raises(ValueError):
        parse_version("3.a")


# it's better to have explicit messages here rather than creating __init__ in a custom exception class
# because the exception becomes not round-trip pickleable
@pytest.mark.parametrize(
    ("s", "expected_msg"), (("3", "Expected #.# but got '3'"), ("3.6.0", "Expected #.# but got '3.6.0'"))
)
def test_parse_version_failure_wrong_segment_count(s, expected_msg):
    # you can catch a tuple of exceptions but it's better to catch one at a time
    # it's better not use match because it can be easy to mess up regex expression
    with pytest.raises(VersionError) as excinfo:
        parse_version(s)
    (msg,) = excinfo.value.args
    assert msg == expected_msg
