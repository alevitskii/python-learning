import contextlib
import sys
from typing import IO


@contextlib.contextmanager
def empty():
    yield


def output_line(s: str, stream: IO[str], *, filename: str | None = None) -> None:
    # option 1
    if filename is not None:
        with open(filename, "w") as f:
            for output_stream in (f, stream):
                output_stream.write(f"{s}\n")
    else:
        stream.write(f"{s}\n")

    # option 2
    if filename is not None:
        # there could be an error after openning it
        # so it's not a good option
        f = open(filename, "w")
        streams = (stream, f)
        ctx = f
    else:
        streams = (stream,)
        # ctx = empty()
        ctx = contextlib.nullcontext()
    with ctx:
        for output_stream in streams:
            output_stream.write(f"{s}\n")

    # option 3 (LOOKS LIKE THE BEST OPTION)
    # ExitStack tears down only successfully entered contexts
    with contextlib.ExitStack() as ctx:
        streams = [stream]
        if filename is not None:
            streams.append(ctx.enter_context(open(filename, "w")))
        for output_stream in streams:
            output_stream.write(f"{s}\n")


def main() -> None:
    output_line("hello world", stream=sys.stdout)
    output_line("hello world", stream=sys.stdout, filename="log.log")


if __name__ == "__main__":
    main()
