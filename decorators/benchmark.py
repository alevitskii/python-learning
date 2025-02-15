import functools
import logging
from collections.abc import Callable
from math import sqrt
from time import perf_counter

logger = logging.getLogger("my_app")


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    for element in range(2, int(sqrt(number)) + 1):
        if number % element == 0:
            return False
    return True


def with_logging[**P, R](
    func: Callable[P, R], logger: logging.Logger
) -> Callable[P, R]:
    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        logger.info(f"Calling {func.__name__}.")
        value = func(*args, **kwargs)
        logger.info(f"Finished calling {func.__name__}.")
        return value

    return wrapper


def benchmark[**P, R](func: Callable[P, R]) -> Callable[P, R]:
    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        start_time = perf_counter()
        value = func(*args, **kwargs)
        end_time = perf_counter()
        run_time = end_time - start_time
        logging.info(f"Execution of {func.__name__} took {run_time:.2f} seconds.")
        return value

    return wrapper


with_default_logging = functools.partial(with_logging, logger=logger)


@with_default_logging
@benchmark
def count_prime_numbers(upper_bound: int) -> int:
    count = 0
    for number in range(upper_bound):
        if is_prime(number):
            count += 1
    return count


def main() -> None:
    logging.basicConfig(level=logging.INFO)
    value = count_prime_numbers(100000)
    logging.info(f"Number of primes: {value}")


if __name__ == "__main__":
    main()
