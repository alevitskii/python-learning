import contextlib

run = print


def stop_database():
    run("systemctl stop postgresql.service")


def start_database():
    run("systemctl start postgresql.service")


class DBHandler:
    def __enter__(self):
        stop_database()
        return self

    def __exit__(self, exc_type, ex_value, ex_traceback):
        start_database()


class dbhandler_decorator(contextlib.ContextDecorator):
    def __enter__(self):
        stop_database()
        return self

    def __exit__(self, ext_type, ex_value, ex_tracebook):
        start_database()


def db_backup():
    run("pg_dump database")


@dbhandler_decorator()
def offline_backup():
    run("pg_dump database")


def offline_backup_2():
    with dbhandler_decorator():
        run("pg_dump database")


def main():
    with DBHandler():
        db_backup()
    offline_backup()
    offline_backup_2()


if __name__ == "__main__":
    main()
