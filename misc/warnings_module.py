# with "python -W error -m <app>" or "PYTHONWARNINGS=error python -m <app>"
# you can turn warnings into exceptions during runtime
import warnings


# it's recommended to set stacklevel to at least 2,
# by default warning points at the line of code where
# the warning is emitted
def foo() -> None:
    warnings.warn("foo is deprecated", SyntaxWarning, stacklevel=2)
    warnings.warn("foo is deprecated", stacklevel=2)
    warnings.warn("foo is deprecated", DeprecationWarning, stacklevel=2)


def main() -> int:
    for _ in range(5):
        foo()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
