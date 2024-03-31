# it's usually not needed to handle sigterm gracefully
# maybe when your program manages processes
import signal
import time
from types import FrameType, TracebackType
from typing import Self


class C:
    def __enter__(self) -> Self:
        return self

    def __exit__(
        self,
        tp: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> None:
        print("world")


class SigTerm(SystemExit):
    pass


def term_cb(signal: int, frame: FrameType | None) -> None:
    raise SigTerm(1)


def main() -> int:
    signal.signal(signal.SIGTERM, term_cb)
    with C():
        time.sleep(100)
        print("hello")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
