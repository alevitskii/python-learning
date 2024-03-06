from typing import LiteralString


def run_query(sql: LiteralString) -> None:
    pass


def caller(arbitrary_string: str, query_string: LiteralString, table_name: LiteralString) -> None:
    run_query("SELECT * FROM students")  # OK
    run_query(query_string)  # OK
    run_query("SELECT * FROM " + table_name)  # OK
    run_query(arbitrary_string)  # error
    run_query(f"SELECT * FROM students where name = {arbitrary_string}")  # error
