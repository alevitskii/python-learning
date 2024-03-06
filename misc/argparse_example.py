# python .\argparse_example.py --help
import argparse
import pprint
from typing import Sequence


def positive_int(s: str) -> int:
    try:
        value = int(s)
    except ValueError:
        raise argparse.ArgumentTypeError(f"expected integer, got {s!r}")

    if value <= 0:
        raise argparse.ArgumentTypeError(f"expected positive integer, got {value}")

    return value


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()

    # positional
    # - help
    # parser.add_argument("filename", help="configuration filename %(prog)s")

    # optional
    # - short vs long opts
    # - aliases
    # - defaults
    # parser.add_argument(
    #     "-c",
    #     "--config",
    #     "--jsonfile",
    #     # required=True,
    #     default="config.json",
    #     help="specify the config file. (default: %(default)s)",
    # )

    # types
    # parser.add_argument("--days", type=int)

    # custom types
    # parser.add_argument("--days", type=positive_int)

    # count
    # -vvv will produce 3, --verbose --verbose will produce 2
    # parser.add_argument("-v", "--verbose", action="count", default=0)

    # boolean options
    # default False, with --force produce True, store_false will do the opposite
    # parser.add_argument("--force", action="store_true")
    # parser.add_argument("--force", action="store_false")
    # will store const in force if --force is used
    # parser.add_argument("--force", action="store_const", const=1)

    # append
    # without specifying default will also work, but default will be None
    # parser.add_argument("--log", action="append", default=[])

    # choices
    # parser.add_argument("--color", choices=("auto", "always", "never"))

    # sub-commands
    # python .\argparse_example.py status --help
    # python .\argparse_example.py checkout --help
    # it's like nested arg parsers
    # subparsers = parser.add_subparsers(dest="command", required=True)

    # status_parser = subparsers.add_parser("status", help="show status")
    # status_parser.add_argument("--force", action="store_true")

    # checkout_parser = subparsers.add_parser("checkout", help="lots of stuff")
    # checkout_parser.add_argument("--verbose", action="count")

    args = parser.parse_args(argv)

    pprint.pprint(vars(args))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
