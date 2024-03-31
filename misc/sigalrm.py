# alarm is global in the process so you need to make sure that
# you don't set timeout in many places in code or handle them
# in many places in code
import contextlib
import signal
import time
from types import FrameType
from typing import Generator


class TimeoutError(Exception):
    pass


def alarm_handler(signum: int, frame: FrameType | None) -> None:
    print(signum, frame)
    raise TimeoutError()


@contextlib.contextmanager
def timeout(s: int) -> Generator[None, None, None]:
    orig = signal.signal(signal.SIGALRM, alarm_handler)
    signal.alarm(s)
    try:
        yield
    finally:
        # there is actually a race between finally and alarm disabling
        # your may get a timeout error anyway
        signal.alarm(0)
        signal.signal(signal.SIGALRM, orig)


def main() -> int:
    with timeout(1):
        time.sleep(2)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
