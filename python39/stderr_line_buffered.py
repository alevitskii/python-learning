import sys
import time


# in python <3.9 if used in pipe
# it'd buffer the whole output and show everything in the end
# in python >3.8 it now buffers per line
def main() -> None:
    for i in range(10):
        print(f"log line {i}", file=sys.stderr)
        time.sleep(0.25)


if __name__ == "__main__":
    main()
