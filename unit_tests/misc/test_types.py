import sys

import pytest


def test_pass():
    assert 1 == 1


def test_failed():
    assert 1 == 2


@pytest.fixture
def fixture():
    # yield  # passed during setup, errored during teardown
    assert False


def test_errored(fixture):
    assert 1 == 1


@pytest.mark.skip(reason="reasonable")
def test_skipped():
    pass


@pytest.mark.skipif(sys.platform == "linux", reason="windows behaviour")
def test_skipped_conditionally():
    pass


@pytest.mark.xfail
def test_expected_to_fail():
    assert False


# @pytest.mark.xfail(strict=True)  # with strict it fails if the test function passes
@pytest.mark.xfail
def test_expected_to_fail_but_passing():
    pass


@pytest.mark.xfail(sys.platform == "linux", reason="windows behaviour")
def test_expected_to_fail_conditionally():
    assert False
