import contextlib

# from contextlib import nullcontext as did_not_raise
import math

import pytest


def f(x: float) -> float:
    return math.sqrt(x)


# usually it's better to test successful and failing scenarious separately
@pytest.mark.parametrize(
    ("input_val", "cm"),
    (
        (-5, pytest.raises(ValueError)),
        (1, contextlib.nullcontext()),
    ),
)
def test_f_errors(input_val, cm):
    with cm:
        f(input_val)


def g():
    cond = ...
    if cond:
        cm = contextlib.nullcontext()
    else:
        cm = open("/dev/null")
    # it's better to use exit stack, because cm desciptor may get leaked
    # before the with clause
    with cm as f:
        ...

    with contextlib.ExitStack() as ctx:
        if not cond:
            f = ctx.enter_context(open("/dev/null"))
            print(f)
