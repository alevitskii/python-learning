# it's recommended to organize the package as follows
# /package/t.py
# /tests/t_test.py

# it's recommended to include __init__.py in tests/ anyway although
# pytest will recognize everything without it, but it won't be building
# an hierarchy (internal implementation), so if you have 2 files with
# the same name, they'll collide (as per one of the core developers)

from typing import NamedTuple

import pytest
from package.t import square


class Case(NamedTuple):
    input_x: int
    expected: int


@pytest.mark.parametrize(
    ("input_n", "expected"),
    (
        (5, 25),
        pytest.param(6, 36, id="square of 6"),
        Case(input_x=7, expected=49),
        (3.0, 9.0),
    ),
)
def test_square(input_n, expected):
    # python hides print by default, use -s to see
    print(f"{input_n=}")
    assert square(input_n) == expected


@pytest.mark.parametrize(
    "input_n",
    ("a", (), []),
)
def test_square_error(input_n):
    with pytest.raises(TypeError):
        square(input_n)


def test_square_float():
    assert square(3.0) == pytest.approx(9.0)


# it's usually better to write functions then classes
# and split into modules if you need grouping
class TestSquare:
    def test_square(self):
        assert square(3) == 9
