import contextlib
import os
import unittest


class TestThing(unittest.TestCase):
    def setUp(self) -> None:
        return self.enterContext(contextlib.chdir("C:/Users"))

    def test_thing(self):
        print("hi from test")
        print(f"cwd: {os.getcwd()}")


def main() -> None:
    unittest.main()


if __name__ == "__main__":
    main()
