import pytest

# @pytest.mark.parametrize(
#     ("a", "b", "c", "d"),
#     (
#         (True, True, True, True),
#         (False, True, True, True),
#         # ...
#         (False, False, False, False),
#     ),
# )
# def test_thing(a, b, c, d): ...


# @pytest.mark.parametrize("a", (True, False))
# @pytest.mark.parametrize(
#     ("b", "c", "d"),
#     (
#         (True, True, True),
#         (True, True, False),
#         # ...
#         (False, False, False),
#     ),
# )
# def test_thing(a, b, c, d): ...


# @pytest.mark.parametrize("a", (True, False))
# @pytest.mark.parametrize("b", (True, False))
# @pytest.mark.parametrize("c", (True, False))
# @pytest.mark.parametrize("d", (True, False))
# def test_thing(a, b, c, d): ...


@pytest.mark.parametrize("a", [pytest.param(True, id="a"), pytest.param(False, id="not_a")])
@pytest.mark.parametrize("b", [pytest.param(True, id="b"), pytest.param(False, id="not_b")])
@pytest.mark.parametrize("c", [pytest.param(True, id="c"), pytest.param(False, id="not_c")])
@pytest.mark.parametrize("d", [pytest.param(True, id="d"), pytest.param(False, id="not_d")])
def test_thing(a, b, c, d): ...
