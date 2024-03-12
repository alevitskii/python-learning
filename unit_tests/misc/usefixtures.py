import functools
import shutil
from unittest import mock

import pytest


@functools.lru_cache(maxsize=1)
def get_default_version() -> str:
    if shutil.which("ruby") and shutil.which("gem"):
        return "system"
    return "default"


# @pytest.fixture(autouse=True)  # you can also use this, but it'll run for every test
@pytest.fixture
def clear_lru_cache():
    get_default_version.cache_clear()
    yield
    get_default_version.cache_clear()


# with passing clear_lru_cache as an argument when it's unused
# static analysis tool may complain
def test_neither_ruby_nor_gem_exist(clear_lru_cache):
    with mock.patch.object(shutil, "which", return_value=None):
        assert get_default_version() == "default"


# with usefixtures it won't
@pytest.mark.usefixtures("clear_lru_cache")
def test_both_ruby_and_gem_exist():
    with mock.patch.object(shutil, "which", return_value="/some/exe"):
        assert get_default_version() == "system"


# Another way is to bypass the cache by accessing __wrapped__ function
def test_neither_ruby_nor_gem_exist2():
    with mock.patch.object(shutil, "which", return_value=None):
        assert get_default_version.__wrapped__() == "default"


def test_both_ruby_and_gem_exist2():
    with mock.patch.object(shutil, "which", return_value="/some/exe"):
        assert get_default_version.__wrapped__() == "system"


def main() -> None:
    print(get_default_version())
    print(get_default_version())


if __name__ == "__main__":
    main()
