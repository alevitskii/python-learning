def exception_group():
    exec_gr = ExceptionGroup(
        "ExceptionGroup Message!",
        [
            FileNotFoundError("This File is not found"),
            ValueError("Invalid Value Provided"),
            ZeroDivisionError("Trying to divide by 0"),
        ],
    )
    raise exec_gr


def nested_exception_group():
    exec_gr = ExceptionGroup(
        "ExceptionGroup Message!",
        [
            FileNotFoundError("This File is not found"),
            ValueError("Invalid Value Provided"),
            ZeroDivisionError("Trying to divide by 0"),
            ExceptionGroup(
                "This is a Nested ExceptionGroup",
                [
                    IndentationError("Please check your Indentation"),
                    SyntaxError("there is a error in the syntax"),
                    ImportError("Module Not Found"),
                ],
            ),
        ],
    )
    raise exec_gr


def main() -> None:
    exception_group()

    try:
        exception_group()
    except ExceptionGroup as eg:
        print(eg.exceptions)

    try:
        exception_group()
    except* FileNotFoundError as fnf:
        print(fnf.exceptions)
    except* ValueError as ve:
        print(ve.exceptions)
    except* ZeroDivisionError as zde:
        print(zde.exceptions)

    nested_exception_group()


if __name__ == "__main__":
    main()
