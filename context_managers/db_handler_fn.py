import contextlib

run = print


def stop_database():
    run("systemctl stop postgresql.service")


def start_database():
    run("systemctl start postgresql.service")


def db_backup():
    run("pg_dump database")


@contextlib.contextmanager
def db_handler():
    try:
        stop_database()
        yield
    finally:
        start_database()


def main() -> None:
    with db_handler():
        db_backup()
    with contextlib.suppress(ValueError):
        # Ok to use when we know it is safe to ignore them
        print("Supress")
        raise ValueError("Supressed")


if __name__ == "__main__":
    # main()
    arns = [1, 2, 3, 4, 5, 6, 7]
    evens = filter(None, (arn % 2 or True for arn in arns))
    print(list(evens))
